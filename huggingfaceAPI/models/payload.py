from typing import Optional
from pydantic import BaseModel, Field


class TextGenerationPredictPayload(BaseModel):
    text: str
    max_length: Optional[int] = Field(50, title="The maximum length of the sequence to be generated.")
    # # min_length: Optional[int] = None
    do_sample: Optional[bool] = Field(False, title="Whether or not to use sampling ; use greedy decoding otherwise.")
    early_stopping: Optional[bool] = Field(False,
                                           title="Whether to stop the beam search when at least num_beams sentences are finished per batch or not.")
    num_beams: Optional[int] = Field(1, title="Number of beams for beam search. 1 means no beam search.")
    temperature: Optional[float] = Field(1.0, title="The value used to module the next token probabilities.")
    top_k: Optional[int] = Field(50, title="The number of highest probability vocabulary tokens to keep for top-k-filtering.")
    top_p: Optional[float] = Field(1.0, title="If set to float < 1, only the most probable tokens with probabilities that add up to top_p or higher are kept for generation.")
    # # repetition_penalty: Optional[float] = None
    # # length_penalty: Optional[float] = None
    no_repeat_ngram_size: Optional[int] = Field(0, title="If set to int > 0, all ngrams of that size can only occur once.")
    num_return_sequences: Optional[int] = Field(1, title="The number of independently computed returned sequences for each element in the batch.")
