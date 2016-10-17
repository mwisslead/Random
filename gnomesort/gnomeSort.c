void gnomeSort(void *data, int size, int nmemb, int (comp)(void *, void *), void (swap)(void *, void *))
{
	int pos = size;
	while (pos < nmemb*size){
		if (comp(data+pos, data+pos-size)){
			pos += size;
		}else{
			swap(data+pos, data+pos-size);
			if (pos > size){
				pos -= size;
			}
		}
	}
}
