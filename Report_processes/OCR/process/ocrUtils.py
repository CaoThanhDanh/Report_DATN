from utils import Utils
import re
import os

class OcrUtils(object):
    @staticmethod
    def exportResult(input_img: str, output_result: str, text: str):
        '''
            Export Result creates or adds results to a txt file to store OCR post-processing results

            Args:
            - input_img: Input file path for OCR processing. Ex: r'simple_0.png'
            - output_result: File path to save OCR results. Ex: r'results_text.txt'
            - text: Text is extracted from the image. Ex: 'This is Example'

            Data Structures:
                #{index}

                {input_img}

                |

                {text}

                |

                #{index}
        '''
        # # Default value
        # input_img = r'simple_0.png'
        # text = 'Cao Thành Danh'
        # output_result = r'file_text.txt'
        
        index = 1
        result = ''

        if os.path.exists(output_result):
            # Check current Data
            old_result = Utils.readAllText(filePath= output_result).strip()
            lines = old_result.split('\n')

            if lines != ['']:
                # The file already exists and is not empty
                encode_pattern_id = r'#(\d+)'
                old_id = int(re.findall(encode_pattern_id, lines[-1])[0])
                index = old_id + 1

                encode = f'#{index}\n{input_img}\n|\n{text}\n|\n#{index}\n'
                result = old_result + '\n' + encode
                pass

            else:
                # The file already exists and is empty
                encode = f'#{index}\n{input_img}\n|\n{text}\n|\n#{index}\n'
                result = encode
        else:
            # File does not exist yet
            encode = f'#{index}\n{input_img}\n|\n{text}\n|\n#{index}\n'
            result = encode

        Utils.writeAllText(filePath= output_result, text= result)
