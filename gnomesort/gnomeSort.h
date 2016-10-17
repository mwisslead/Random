#ifndef GNOMESORT_H
#define GNOMESORT_H

void gnomeSort(void *data, int size, int nmemb, int (comp)(void *, void *), void (swap)(void *, void *));

#endif
