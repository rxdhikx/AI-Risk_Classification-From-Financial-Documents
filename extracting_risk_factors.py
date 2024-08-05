#WORKING FINE even for unformatted/uncleaned paras where page numbers and "table of contents" is mentioned in between the sentences, abruptly

import os
import codecs
import pandas as pd
import re
import word_list_AI as _input_list
import nltk

# Set NLTK data path
nltk.data.path.append('/Users/rravindra0463/Desktop/ai_proj/venv/nltk_data')

from nltk.tokenize import sent_tokenize

# Define paths
_PARENT_PATH = os.path.join(os.path.dirname(__file__), 'test') #folder with 10-20 financial reports, 2 are related to AI
_OUTPUT_PATH = os.path.join(os.path.dirname(__file__), 'output') #output folder path
_OUTPUT_FILENAME = 'test.csv'  #output file name
_KEYWORD_LIST = _input_list._AI_LIST_v3  #specified AI related keywords

def extract_text_between_keywords(text, start_keyword, end_keyword):
    pattern = re.compile(r'{}(.*?){}'.format(re.escape(start_keyword), re.escape(end_keyword)),
                         re.DOTALL | re.IGNORECASE)
    matches = pattern.search(text)
    if matches:
        return matches.group(1).strip()
    else:
        return ''

#extracting risk factor section. it is present in between the item 1a and item 1b of the financial reports. Hence we use this as start and end keyword to extract everything in between 
def summary_textual_extract(text, keywords, start_keyword='', end_keyword=''):
    if start_keyword and end_keyword:
        start_occurrences = [match.start() for match in re.finditer(re.escape(start_keyword), text, re.IGNORECASE)]
        end_occurrences = [match.end() for match in re.finditer(re.escape(end_keyword), text, re.IGNORECASE)]

        if len(start_occurrences) >= 2 and len(end_occurrences) >= 2:
            last_start = start_occurrences[1] if len(start_occurrences) > 1 else start_occurrences[0]
            last_end = end_occurrences[1] if len(end_occurrences) > 1 else end_occurrences[0]

            if last_start < last_end:
                extract_text = text[last_start + len(start_keyword):last_end].strip()
            else:
                extract_text = ''
        else:
            extract_text = ''
    else:
        extract_text = text

    has_item = 1 if extract_text else 0
    word_count = len(re.findall(r'\b\w+\b', extract_text))

    return has_item, extract_text, word_count

#cleaning the text - some paragraphs are not continuous, since they are in html formatted document it consists of page numbers and "table of contents" as header in between the 
#sentences abruptly, in our pre-cleaned file. thus we need to ensure it is cleaned before proceeding, for accurate extractions.
def clean_text(text):
    text = re.sub(r'\btable of contents\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s*\d+\s*', ' ', text)  # Remove standalone numbers (e.g., page numbers)
    text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespace with a single space
    return text.strip()

#after extracting, save only those risk factor sections which are related to AI, parsed through keywords
def find_ai_sentences(item_1a_text, keywords):
    sentences = sent_tokenize(item_1a_text)
    ai_sentences = []
    for i, sentence in enumerate(sentences):
        if any(keyword in sentence for keyword in keywords):
            context_r3 = sentences[max(0, i - 3):i + 4]
            context_r5 = sentences[max(0, i - 5):i + 6]
            ai_sentences.append({
                'Sentence': sentence,
                'SentencesR3': ' '.join(context_r3),
                'SentencesR5': ' '.join(context_r5),
                'KeywordMentioned': ', '.join([keyword for keyword in keywords if keyword in sentence])
            })
    return ai_sentences

if __name__ == '__main__':
    rows = []
    processed_files = set()  # Set to keep track of processed files

    try:
        for file_name in os.listdir(_PARENT_PATH):
            file_path = os.path.join(_PARENT_PATH, file_name)
            
            if os.path.isfile(file_path) and '10-K' in file_name:
                if file_name in processed_files:
                    continue  # Skip if the file has already been processed

                print(f"Processing file: {file_path}")

                file_info = file_name.split('_')
                if len(file_info) >= 6:
                    type_10_x = file_info[1]
                    if type_10_x in _input_list.f_10K:
                        with codecs.open(file_path, 'r', 'utf-8') as file_obj:
                            file_text = file_obj.read().lower()

                        # Extract Item 1A text
                        has_item1a, item_1a_text, word_count_1a = summary_textual_extract(file_text, _KEYWORD_LIST, start_keyword='item 1a', end_keyword='item 1b')
                        if has_item1a:
                            # Clean the extracted text
                            item_1a_text = clean_text(item_1a_text)
                            
                            # Find AI-related sentences
                            ai_sentences = find_ai_sentences(item_1a_text, _KEYWORD_LIST)
                            
                            if ai_sentences:  # Only add rows if AI sentences are found
                                rows.append({
                                    'filename': file_name,
                                    'Item1A': item_1a_text,
                                    'Sentence': '',
                                    'SentencesR3': '',
                                    'SentencesR5': '',
                                    'KeywordMentioned': ''
                                })
                                
                                for ai_sentence in ai_sentences:
                                    if ai_sentence['KeywordMentioned']:  # Ensure the KeywordMentioned field is not empty
                                        rows.append({
                                            'filename': file_name,
                                            'Item1A': item_1a_text,
                                            'Sentence': ai_sentence['Sentence'],
                                            'SentencesR3': ai_sentence['SentencesR3'],
                                            'SentencesR5': ai_sentence['SentencesR5'],
                                            'KeywordMentioned': ai_sentence['KeywordMentioned']
                                        })
                                
                                processed_files.add(file_name)  # Mark this file as processed
                        else:
                            print(f"No Item 1A section found in file: {file_path}")
                    else:
                        print(f"File type is not 10-K: {file_name}")
                else:
                    print(f"Unexpected file naming format: {file_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Convert list of rows to DataFrame and filter out incomplete rows
    output_file = pd.DataFrame(rows)
    output_file = output_file[output_file['KeywordMentioned'].str.strip() != '']  # Filter rows where KeywordMentioned is not empty
    output_file.to_csv(os.path.join(_OUTPUT_PATH, _OUTPUT_FILENAME), index=False)
    print('Processing complete. Output saved to:', os.path.join(_OUTPUT_PATH, _OUTPUT_FILENAME))
