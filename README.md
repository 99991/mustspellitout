# LLMs must spell it out

This repository showcases a phenomenon where LLMs struggle to answer simple questions about whether the birth year of a famous person is even or odd. However, when asked to provide the birth year and then determine whether it is even or odd, they perform flawlessly. This repository serves as a demonstration of this phenomenon.

## Examples

#### Even or odd without birth year (❌ Incorrect)

> User: Is the birth year of Arnold Schwarzenegger even or odd? Answer only with "even" or "odd", nothing else.
> 
> ChatGPT: Even

#### Asking for birth year first and only then for even or odd (✅ Correct)

> User: What is the birth year of Arnold Schwarzenegger? Is it even or odd? Answer only with the birth year and  "even" or "odd", nothing else.
> 
> ChatGPT: 1947, odd

## Files

* `ground_truth.csv` contains `name,birth_year` pairs of famous people and their birth years, generated using ChatGPT and cross-checked against the output of `llama-3.1-70b-versatile` using the [Groq API](https://console.groq.com/docs/openai). Only a single birth year was different; Llama incorrectly predicted Jack Nicholson's birth year as 1938 instead of 1937.
* `chatgpt_name_birth_year_odd.csv` and `llama_70b_name_birth_year_odd.csv` contain `name,birth_year_odd` pairs, where `birth_year_odd` is 1 if the birth year is odd and 0 otherwise. The prompt used to generate these files was: `For the following people, give a csv with (name, birth_year_odd) where birth_year_odd is 1 if the birth year is odd and 0 if the birth year is even.`
* `chatgpt_name_birth_year_birth_year_odd.csv` and `llama_70b_name_birth_year_birth_year_odd.csv` contain `name,birth_year,birth_year_odd` triplets. The prompt used to generate these files was: `For the following people, give a csv with (name, birth_year, birth_year_odd) where birth_year_odd is 1 if the birth year is odd and 0 if the birth year is even.`
* `main.py` reads all the CSV files and counts the number of correct values for `birth_year_odd`.

## Results

| Correct guesses | Odd guesses | Filename |
| --- | --- | --- |
| 55 | 93 | `llama_70b_name_birth_year_odd.csv` |
| 56 | 41 | `chatgpt_name_birth_year_odd.csv` |
| 99 | 54 | `llama_70b_name_birth_year_birth_year_odd.csv` |
| 100 | 55 | `chatgpt_name_birth_year_birth_year_odd.csv` |

## Discussion

* LLMs perform poorly when guessing whether a famous person's birth year is odd, with accuracy barely above chance.
* LLMs are highly accurate when guessing the birth year of famous people, with only one incorrect prediction by `llama-3.1-70b-versatile`.
* LLMs are perfect when guessing whether a famous person's birth year is odd **when provided with the birth year beforehand**. This means that LLMs should be instructed to write all relevant information about a certain topic before asking them to reason about it.
* `llama-3.1-70b-versatile` guessed odd birth years disproportionately often, suggesting that asking for an entire CSV file at once introduces a bias. ChatGPT shows a small bias in the opposite direction.

## Citations

More similar experiments can be found in

* [Physics of Language Models: Part 3.2, Knowledge Manipulation](https://arxiv.org/abs/2309.14402) by Zeyuan Allen-Zhu and Yuanzhi Li
* [Rephrase and Respond: Let Large Language Models Ask Better Questions for Themselves](https://arxiv.org/abs/2311.04205) by Yihe Deng, Weitong Zhang, Zixiang Chen, and Quanquan Gu

BibTeX citations:

```bibtex
@misc{allenzhu2024physicslanguagemodels32,
  title={Physics of Language Models: Part 3.2, Knowledge Manipulation},
  author={Zeyuan Allen-Zhu and Yuanzhi Li},
  year={2024},
  eprint={2309.14402},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2309.14402},
}

@misc{deng2024rephraserespondletlarge,
  title={Rephrase and Respond: Let Large Language Models Ask Better Questions for Themselves},
  author={Yihe Deng and Weitong Zhang and Zixiang Chen and Quanquan Gu},
  year={2024},
  eprint={2311.04205},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2311.04205},
}
```
