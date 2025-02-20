# EuskañolDS: A Naturally Sourced Corpus for Basque-Spanish Code-Switching
Code-switching (CS) remains a significant challenge in Natural Language Processing (NLP), mainly due a lack of relevant data. In the context of the contact between the Basque and Spanish languages in the north of the Iberian Peninsula, CS frequently occurs in both formal and informal spontaneous interactions. However, resources to analyse this phenomenon and support the development and evaluation of models capable of understanding and generating code-switched language for this language pair are almost non-existent. We introduce a first approach to develop a naturally sourced corpus for Basque-Spanish code-switching. Our methodology consists of identifying CS texts from previously available corpora using language identification models, which are then manually validated to obtain a reliable subset of CS instances.

This repository contains the code used to generate the dataset *EuskañolDS*.

## Download Dataset
The dataset can be downloaded at: https://ixa2.si.ehu.eus/mheredia/euskanolds

The dataset can also be accessed through HuggingFace: https://huggingface.co/datasets/maihered/EuskanolDS

## Source Datasets


| Name                                                                            | Size(Tokens) | Source                                    | Topics                               |
|---------------------------------------------------------------------------------|-------------:|-------------------------------------------|--------------------------------------|
| [BasqueParl](https://github.com/ixa-ehu/basqueparl)                             |          14M | Parliamentary transcriptions              | Political discourse                  |
| [Heldugazte](https://github.com/ixa-ehu/heldugazte-corpus)                      |          37M | Twitter                                   | News, sport, music, nationalist left |
| [Covid-19](https://github.com/joseba-fdl/basque_twitter_covid19_corpus)         |          57M | Twitter (September 2019 to February 2021) | Covid-19, political issues           |

## Dataset 

Description:

| Split  |  Tokens | Instances | Avg. Length |
|--------|--------:|----------:|------------:|
| Silver | 537,648 |    20,008 |       26.87 |
| Gold   |  36,860 |       927 |       39.76 |

Examples from the dataset:

|       Source       |                                                                                         Instance                                                                                        |                                                          Translation                                                          |    Type of CS    |
|:------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|:----------------:|
|     HelduGazte     |                                    bihar zazpi terditan gora y yo me muerooooooo                                    |                                   tomorrow up at seven thirty and i'm going to die                                   | Intra-sentential |
| BasqueParl | Por lo tanto, no tengo nada más que añadir. Eta eskerrik asko denoi akordio batera heldu garelako. | Therefore, I don't have anything else to add. And thank you everyone for having reached an agreement. | Inter-sentential |
|      Covid-19      |                                Katxis!Veo a la tropa baja... Eutsi goiari!                              |                                     Heck! I see the spirits are low... Cheer up!                                     |    Emblematic    |

## Scripts
Example usage:

```
python scripts/lid.py --input_file "file.tsv" --text_field "text_field"
```

## Citation
The [paper](https://arxiv.org/abs/2502.03188) that explains the dataset and experiments can be cited as follows:
```
@misc{heredia2025euskanolds,
      title={Euska\~nolDS: A Naturally Sourced Corpus for Basque-Spanish Code-Switching}, 
      author={Maite Heredia and Jeremy Barnes and Aitor Soroa},
      year={2025},
      eprint={2502.03188},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.03188}, 
}
```
