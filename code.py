"All The Code Is Done On Google Colab Where Drive Is Mounted  To Use Test Csv'
from google.colab import drive
drive.mount('/content/drive')

"Loading The Test CSV"

import pandas as panda
test=panda.read_csv('/content/drive/MyDrive/testt.csv')
test.head()

"Exporting two column data ID and its random generated corresponding label from the above test csv into submission csv file."

test=panda.read_csv('/content/drive/MyDrive/testt.csv', usecols=['id','target'])
test.head()

"Creating Our Csv File With That Two Exported Columns For Submission On Kaggle"

test.to_csv('submission.csv', index=False)