# Euphonious Article

Score arabic articles based on letters' sound source. 

# How to use

python attractive.py [-h] [-d DATASET] [-m METHOD] [-n MINLEN] [-x MAXLEN]

arguments:

  -h, --help            show this help message and exit
  
  -d DATASET, --dataset DATASET
                        dataset path (file or directory)
  
  -m METHOD, --method METHOD
                        scoring method (average, sum, global_average)
  
  -n MINLEN, --minlen MINLEN
                        article minimum length
  
  -x MAXLEN, --maxlen MAXLEN
                        article maximum length

# Example:
python euphonious.py -d SaudiNewsNet/dataset/2015-07-23.json -m average

يطل عيد الفطر المبارك على الأمة الإسلامية حاملا معه الفرحة والتفاؤل بقدوم مستقبل مشرق كما يجسد العيد مشاعر الرحمة والرأفة بين أفراد المجتمع، وتفاعلا مع هذه المشاعر النبيلة والرقيقة حرصت مستشفى المركز التخصصي الطبي ممثلة بسعادة المدير العام التنفيذي الدكتور /خالد مكيمن السبيعي على مشاركة المرضى المنومين بالمستشفى فرحتهم بالعيد والتخفيف من آلامهم، إيمانا بأن هذا الدور الإنساني بجانب العلاج الطبي يجب أن تقوم به جميع المستشفيات تجاه مرضاهم لما له من أثر كبير في رفع الروح المعنوية لدى المرضى وكذلك سعادتهم بوجود أسرة المستشفى معهم في هذا اليوم المبارك وانطلاقا من هذا المفهوم وتجسيدا للمشاعر المخلصة والصادقة قام وفد طبي وإداري من المستشفى يتقدمهم المدير العام التنفيذي بزيارة المرضى على الأسرة البيضاء للاطمئنان على أحوالهم وتقديم التهنئة بالعيد السعيد مصحوبة بالدعوات القلبية لهم بالشفاء العاجل. وقد استقبل المرضى الوفد بسرور متمنين للمستشفى دوام الازدهار والتقدم. 

# Dataset Source

You may download a sample dataset of a news articles from 

https://github.com/ParallelMazen/SaudiNewsNet
