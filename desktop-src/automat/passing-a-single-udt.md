---
title: Passing a Single UDT
description: For passing a single UDT for v-table binding, the designer of the server describes the data types of the UDT in a IDL file. The client and server will then simply declare the UDT and pass it to one another.
ms.assetid: 909a177a-59b5-45ab-8990-2f8c384fcb07
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

[**GetRecordInfoFromTypeInfo**](/windows/previous-versions/OleAuto/nf-oleauto-getrecordinfofromtypeinfo?branch=master)
</dt> <dt>

[**GetRecordInfoFromGuids**](/windows/previous-versions/OleAuto/nf-oleauto-getrecordinfofromguids?branch=master)
</dt> <dt>

[**LoadRegTypeLib**](/windows/previous-versions/OleAuto/nf-oleauto-loadregtypelib?branch=master)
</dt> <dt>

[**IDispatch::GetTypeInfo**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-gettypeinfo?branch=master)
</dt> <dt>

[**ITypeInfo**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo?branch=master)
</dt> </dl>

 

 




