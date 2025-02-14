# ProbPrefix
Probabilistic Prefix Search


This Script make infinite loop continuously generates random private keys within the specified range and converts them to hashed addresses.

If the random number falls within a previously checked range, it skips to the next iteration.

The address generated from the random private key is compared to the target.

If an exact match is found, the private key and address are written to TargetFound.txt and the loop breaks.

If a partial match is found (determined by the chk_p function), the range around the random number is calculated and skipped in the future by adding it to the HashTable.

This script essentially performs a brute-force search for a hash that matches a given target hash. It uses ranges to optimize the search by skipping areas that have already been checked.
