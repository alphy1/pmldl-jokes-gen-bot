# pmldl-jokes-gen-bot
Telegram bot that can generate jokes on russian language

## Navigation
* reports - 4 project deliverable reports
* datasets - 1 file with dataset and 2 files that generate datasets from 2 different sources, dataset from anekdoty.ru is too large
* src - 2 jupyter notebooks that contain code to install all dependencies, prepare data and train model
* rugpt3_model.zip - trained on the datasets model, check results using:
```
!python3 generate_transformers.py \
    --model_type=gpt2 \
    --model_name_or_path=rugpt3_model/ \
    --prompt='<s>Какой то текст' \
    --k=10 \
    --num_return_sequences=5 \
    --p=0.95 \
    --length=200
```  

## GPT2 model
ref: https://towardsdatascience.com/teaching-gpt-2-a-sense-of-humor-fine-tuning-large-transformer-models-on-a-single-gpu-in-pytorch-59e8cec40912
* contains preprocessing of jokes, which can be used in lstm
* trained on Google Colab; therefore, we could train only on 5000 samples
* model cannot produce normal words, they are not inherited and seem more like tongue twisters 

Examples:
```
JOKE:Дчто покучали все стороне все стать спискальность, которые стороне все стать спискальность.<|endoftext|> 
JOKE:Когда подать стальют что в когда подать? Вы вы подать помнеть?<|endoftext|> 
JOKE:Рдруживают просто не том приходить на встранность приходить в не том разнают.<|endoftext|> 
JOKE:В всего не ниходительность напомачится напомачится напомачится напомачится.<|endoftext|> 
JOKE:Приставает в нишил в не продавать по подали прованить.<|endoftext|> 
JOKE:Я которые пришение на на порезности пользовить на на пользовить на пользовить.<|endoftext|> 
```

## ruGPT3 model
ref: https://github.com/sberbank-ai/ru-gpts
* we used pretrained on russian language gpt3 model by Sberbank
* for generating input to the model we used Markov chains
* marking `line_by_line` argument as `True` made model work much better
* words are correct and sentences make sense, some of them are even funny
Examples:
```
<s>- Все! Надо срочно что-то менять. Я не могу больше работать.- А ты попробуй, попробуй, не получается?- Ты что?! Это же невозможно!- Почему?- Потому что нельзя.
<s>Я сидел на крыше, когда кто-то из толпы крикнул "Смотри, какая красотка!". И это была не я, а моя жена...
<s>Разговор по мобильному телефону:- У тебя кто-то есть?
<s>Так не все ли равно, что будет, если на Украине не будут уважать русский язык?
<s>Треть россиян поддержали инициативу президента о создании единого пенсионного фонда. Остальные россияне заявили, что не против, но у них нет выбора.
<s>Ясуо это сбалансированный персонаж, который не пьет, не курит, не занимается спортом. Но он же еще и гей!
<s>В иннополисе мальчики, в которых влюбляются девочки, называются гейши.
<s>Как быстро научиться программировать на питоне?Надо взять питона, положить в карман, сказать, что хочешь кушать и уйти.
<s>Когда я увидел даму на флопе, то подумал, что она - моя бывшая.
```