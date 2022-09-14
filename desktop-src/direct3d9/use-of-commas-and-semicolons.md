---
description: Using commas and semicolons can be the most complex syntax issue in the file format, and this usage is very strict. Commas are used to separate array members; semicolons terminate each data item.
ms.assetid: 82582213-907c-4760-a849-e6cf5f6d60bc
title: Use of Commas and Semicolons
ms.topic: article
ms.date: 05/31/2018
---

# Use of Commas and Semicolons

Using commas and semicolons can be the most complex syntax issue in the file format, and this usage is very strict. Commas are used to separate array members; semicolons terminate each data item.

For example, if a template is defined in the following manner:


```
template mytemp {
DWORD myvar;
}
```



Then an instance of this template looks like the following:


```
mytemp dataTemp {
1;
}
```



If a template containing another template is defined in the following manner;


```
template mytemp {
DWORD myvar;
DWORD myvar2;
}
template container {
FLOAT aFloat;
mytemp aTemp;
}
```



Then an instance of this template looks like the following:


```
container dataContainer {
1.1;
2; 
3;;
}
```



Note that the second line that represents the mytemp inside container has two semicolons at the end of the line. The first semicolon indicates the end of the data item, aTemp (inside container), and the second semicolon indicates the end of the container.

If an array is defined in the following manner:


```
Template mytemp {

array DWORD myvar[3];

}
```



Then an instance of this looks like the following:


```
mytemp aTemp {
1, 2, 3;
}
```



In the array example, there is no need for the data items to be separated by semicolons because they are delineated by commas. The semicolon at the end marks the end of the array.

Consider a template that contains an array of data items defined by a template.


```
template mytemp {
DWORD myvar;
DWORD myvar2;
}
template container {
DWORD count;
array mytemp tempArray[count];
}
```



An instance of this would look like the following example.


```
container aContainer {
3;
1;2;,3;4;,5;6;;
}
```



## Related topics

<dl> <dt>

[Text Encoding](text-encoding.md)
</dt> </dl>

 

 



