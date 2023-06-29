# MultiEL
Multilingual Entity Linking model by BELA model

This project want to create easy-to-use Multilingual Entity Linking model by BELA model.

**Origin Project**

- Bi-encoder Entity Linking Architecture (BELA): [https://github.com/facebookresearch/BELA](https://github.com/facebookresearch/BELA)


## Install

> pip install multiel

## Usage

```python
from multiel import BELA

bela_run = BELA(device="cuda")

print(bela_run.process_batch(["นายกประยุทธ์ประกาศจัดการเลือกตั้ง"]))
```

output:
```python
[{'offsets': [0], 'lengths': [12], 'entities': ['Q2108126'], 'md_scores': [0.22365164756774902], 'el_scores': [0.6967974901199341]}]
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
- checkpoint_name: checkpoint name (wiki, aida, mewsli, and e2e)
- device: device
- config_name: config name (in the BELA project)
- repo: Huggingface Hub repo (Default [wannaphong/BELA](https://huggingface.co/wannaphong/BELA))

**Predict**

```python
BELA.process_batch([str, str])
```

## License

MIT license and the model is MIT license. ([BELA is MIT licensed](https://github.com/facebookresearch/BELA/blob/main/LICENSE))
