---
title: Passing a Single UDT
description: For passing a single UDT for v-table binding, the designer of the server describes the data types of the UDT in a IDL file. The client and server will then simply declare the UDT and pass it to one another.
ms.assetid: '909a177a-59b5-45ab-8990-2f8c384fcb07'
---

# Passing a Single UDT

For passing a single UDT for v-table binding, the designer of the server describes the data types of the UDT in a IDL file. The client and server will then simply declare the UDT and pass it to one another.

The following is an example of a type defined for a UDT:


```C++
library udttest
{
   typedef [uuid(C1D3A8C0-A4AA-11D0-819C-00A0C90FFFC3)] struct_tagUDT {
      unsigned long a1;
      BSTR pbstr;
   } UDT;
```



The structure, named **UDT**, is defined with two data types, an unsigned long and a BSTR. The struct tagTEST, which is the UDT, is declared and assigned some values. Error checking is omitted for brevity.


```C++
typedef struct tagTEST {
    ULONG a1;
    BSTR pbstr;
} TEST;
TEST a, b;
a.a1 = 0x1234;
a.pbstr = SysAllocString(L"Hello");
b.a1 = 0;
b.pbstr = NULL;
```



Then the structure is passed to a method:

`pRecInfo->RecordCopy(&a, &b);`

## Related topics

<dl> <dt>

[**GetRecordInfoFromTypeInfo**](getrecordinfofromtypeinfo.md)
</dt> <dt>

[**GetRecordInfoFromGuids**](getrecordinfofromguids.md)
</dt> <dt>

[**LoadRegTypeLib**](loadregtypelib.md)
</dt> <dt>

[**IDispatch::GetTypeInfo**](idispatch-gettypeinfo.md)
</dt> <dt>

[**ITypeInfo**](itypeinfo.md)
</dt> </dl>

 

 




