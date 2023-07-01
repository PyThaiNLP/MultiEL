# MultiEL
Multilingual Entity Linking model by BELA model

This project want to create easy-to-use Multilingual Entity Linking model by BELA model for entity linking in 98 languages.

**Origin Project**

- Bi-encoder Entity Linking Architecture (BELA): [https://github.com/facebookresearch/BELA](https://github.com/facebookresearch/BELA)
- Multilingual End to End Entity Linking: [https://arxiv.org/abs/2306.08896](https://arxiv.org/abs/2306.08896)


## Install

> pip install multiel

## Usage

```python
from multiel import BELA

bela_run = BELA(device="cuda")

print(bela_run.process_batch(["Jobs was CEO of Apple"]))
# output: [{'offsets': [9, 16], 'lengths': [3, 5], 'entities': ['Q484876', 'Q312'], 'md_scores': [0.24852867424488068, 0.7043067216873169], 'el_scores': [0.48497316241264343, 0.9504457712173462]}]
print(bela_run.process_batch(["ジョブズ氏はアップルのCEOだった"]))
# output: [{'offsets': [6, 6, 11], 'lengths': [5, 8, 3], 'entities': ['Q312', 'Q312', 'Q484876'], 'md_scores': [0.8206272721290588, 0.2937866449356079, 0.27033868432044983], 'el_scores': [0.9398021101951599, 0.0239552054554224, 0.4219340682029724]}]
print(bela_run.process_batch(["Jobs war der CEO von Apple"]))
# output: [{'offsets': [13, 21], 'lengths': [3, 5], 'entities': ['Q484876', 'Q312'], 'md_scores': [0.4644337594509125, 0.7975106835365295], 'el_scores': [0.6950674653053284, 0.9626906514167786]}]
print(bela_run.process_batch(["जॉब्स एप्पल के सीईओ थे"]))
# output: [{'offsets': [6, 15], 'lengths': [5, 4], 'entities': ['Q312', 'Q484876'], 'md_scores': [0.5419769883155823, 0.20518577098846436], 'el_scores': [0.8974292874336243, 0.3540962338447571]}]
print(bela_run.process_batch(["จ๊อบเคยเป็นซีอีโอบริษัทแอปเปิล"]))
# output: [{'offsets': [11, 23], 'lengths': [6, 7], 'entities': ['Q484876', 'Q312'], 'md_scores': [0.30301809310913086, 0.6399497389793396], 'el_scores': [0.7142490744590759, 0.8657019734382629]}]
```

#### API

```python
from multiel import BELA

BELA(
 md_threshold:float=0.2,
 el_threshold:float=0.4, 
 checkpoint_name: str="wiki", 
 device: str="cuda:0",
 config_name:str="joint_el_mel_new",
 repo:str="wannaphong/BELA"
)
```

- md_threshold: md threshold
- el_threshold: Entity Linking threshold
- checkpoint_name: checkpoint name (wiki, aida, mewsli, and e2e) or your file name with extension
- device: device
- config_name: config name (in the BELA project)
- repo: Huggingface Hub repo (Default [wannaphong/BELA](https://huggingface.co/wannaphong/BELA))

**Predict**

```python
BELA.process_batch([str, str])
```

## How to train the model?

See more: [Multilingual End to End Entity Linking
](https://github.com/facebookresearch/BELA)
## License

MIT license and the model is MIT license. ([BELA is MIT licensed](https://github.com/facebookresearch/BELA/blob/main/LICENSE))
