# HPC.MapReduce.WordCountAndInvertedIndex

Simulated the MapReduce model locally with Python and Unix pipes, without a Hadoop cluster.

## What I Did

* Traced map, shuffle and sort, and reduce by hand on a small example
* Built Word Count with a mapper and a reducer connected by `sort`
* Added a combiner and compared the amount of intermediate data
* Assigned keys to two reducers with a simple partition function
* Built an inverted index that lists the documents containing each word
* Answered questions on the MapReduce runtime, data locality and HDFS

## Results

### Word Count (input.txt)

The mapper produced 32 key value pairs, and the reducer turned them into 24 unique words.
Most frequent words: data 3, can 3.

### Combiner

For part1.txt the combiner reduced the mapper output from 4 records to 2.
Final result with and without the combiner: data 4, science 3.

### Partitioning (ASCII sum mod 2)

| Key | ASCII sum | Reducer |
|---|---|---|
| data | 410 | R0 |
| science | 730 | R0 |
| parallel | 845 | R1 |
| computer | 879 | R1 |
| hadoop | 635 | R1 |
| reduce | 632 | R0 |

### Inverted Index (documents.txt)

    computing   doc1,doc4
    data        doc2,doc3,doc4
    parallel    doc1,doc3

## Files

| File | Description |
|---|---|
| `mapper.py` | Outputs (word, 1) for every word |
| `reducer.py` | Sums the counts of each word |
| `combiner.py` | Local reducer that runs after one mapper |
| `index_mapper.py` | Outputs (word, document ID) |
| `index_reducer.py` | Collects unique document IDs for each word |
| `input.txt` | Input text for Word Count |
| `documents.txt` | Input documents for the inverted index |
| `output.txt` | Final Word Count output |
| `index_output.txt` | Final inverted index output |

## How to Run

    python3 mapper.py < input.txt | sort | python3 reducer.py > output.txt
    python3 index_mapper.py < documents.txt | sort | python3 index_reducer.py > index_output.txt

## Key Takeaways

* `sort` plays the role of shuffle and sort: it does not count, it only puts equal keys next to each other
* All values of one key must reach one reducer, otherwise the result is split
* A combiner reduces network traffic without changing the result, because addition works in any order
* Moving intermediate data between machines is often the most expensive step

## Tools

* Python 3
* WSL (Ubuntu) + VS Code
