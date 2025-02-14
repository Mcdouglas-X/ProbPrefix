# ProbPrefix
Probabilistic Prefix Search

This technique is based on the compound probability that a specific prefix appears in a set or range of hashes, discarding the less probable percentages.



using **ProbPrefix.py**

This Script make infinite loop continuously generates random private keys within the specified range and converts them to hashed addresses.

If the random number falls within a previously checked range, it skips to the next iteration.

The address generated from the random private key is compared to the target.

If an exact match is found, the private key and address are written to TargetFound.txt and the loop breaks.

If a partial match is found (determined by the chk_p function), the range around the random number is calculated and skipped in the future by adding it to the HashTable.

This script essentially performs a brute-force search for a hash that matches a given target hash. It uses ranges to optimize the search by skipping areas that have already been checked.



using **CreateRanges.py**


In case of having a series of pre-stored prefixes, they are added to the script by copying their private keys to "range.txt".This iterates over private keys obtained from the "range.txt" file, creating a new "Ht.bin" if it does not exist. The found prefixes are added to ranges in case you want to generate a new database using other percentages.


**Disclaimer:** This script is only a demonstration, based on my own statistics which may seem counterintuitive due to the depth of probabilities. It is not intended to be fast either. Create your own version in C and Cuda if you desire an optimal environment. I do not have the resources to explore with Cuda at the moment.


**Donate to:**
**btc: bc1qxs47ttydl8tmdv8vtygp7dy76lvayz3r6rdahu**
