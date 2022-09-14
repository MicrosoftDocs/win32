---
title: Array Attributes
description: There is a close relationship between arrays and pointers in the C language.
ms.assetid: 0d65c993-63e4-42ae-ae24-6c19a71386a1
ms.topic: article
ms.date: 05/31/2018
---

# Array Attributes

There is a close relationship between arrays and pointers in the C language. When passed as a parameter to a function, an array name is treated as a pointer to the first element of the array, as shown in the following example:


```C++
/* fragment */
extern void f1(char * p1);

void main(void)
{
    char chArray[MAXSIZE];

    fLocal1(chArray);
}
```



In a local call, you can use the pointer parameter to march through memory and examine the contents of other addresses:


```C++
/* dump memory (fragment) */
void fLocal1(char * pch1)
{
    int i;

    for (i = 0; i < MAXSIZE; i++)
       printf("%c ", *pch1++);
}
```



When a client passes a pointer to a remote procedure, the client stub transmits both the pointer and the data it points to. Unless the pointer is restricted to its corresponding data, all the client's memory must be transmitted with every remote call. By enforcing strong typing in the interface definition, MIDL limits client-stub processing to the data that corresponds to the specified pointer.

The size of the array and the range of array elements transmitted to the remote computer can be constant or variable. When these values are variable, and thus determined at run time, you must use attributes in the IDL file to specify how many array elements to transmit. The following MIDL attributes support array bounds.



| Attribute                             | Description                                             | Default |
|---------------------------------------|---------------------------------------------------------|---------|
| \[ [**first\_is**](/windows/desktop/Midl/first-is)\]   | Index of the first array element transmitted.           | 0       |
| \[ [**last\_is**](/windows/desktop/Midl/last-is)\]     | Index of the last array element transmitted.            | \-      |
| \[ [**length\_is**](/windows/desktop/Midl/length-is)\] | Total number of array elements transmitted.             | \-      |
| \[ [**max\_is**](/windows/desktop/Midl/max-is)\]       | Highest valid array index value.                        | \-      |
| \[ [**min\_is**](/windows/desktop/Midl/min-is)\]       | Lowest valid array index value.                         | 0       |
| \[ [**size\_is**](/windows/desktop/Midl/size-is)\]     | Total number of array elements allocated for the array. | \-      |



 

> [!Note]  
> The **min\_is** attribute is not implemented in RPC. The minimum array index is always treated as zero.

 

 

 