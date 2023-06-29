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