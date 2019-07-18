# ordered_search_search_engine

The Feeling Lucky question assumed it was enough to find the best-ranked page for a given query. For most queries, though, we don't just want the best page (according to the page ranking algorithm), we want a list of many pages that match the query, ordered from the most likely to be useful to the least likely.

Define a procedure, ordered_search(index, ranks, keyword), that takes the same inputs as lucky_search from Question 5,but returns an ordered list of all the URLs that match the query.

To order the pages, use the quicksort algorithm, invented by Sir Tony Hoare in 1959. Quicksort provides a way to sort any list of data, using an expected number of comparisons that scales as n log n where n is the number of elements in the list.
