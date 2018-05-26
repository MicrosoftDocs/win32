---
title: Describing UDT in the IDL File
description: The designer of the server describes the data types of the UDT in an IDL file.
ms.assetid: 1333a3b4-1fe3-4813-a710-baeb73273bbb
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Describing UDT in the IDL File

The designer of the server describes the data types of the UDT in an IDL file. The IDL file must be compiled using MIDL to generate a type library with UUID set to the UDT. Otherwise MIDL will create an alias and set UUID on that alias. This will generate a header file with the description of the UDT.

The following is an example of a type defined for a UDT:


```C++
library udttest
{
   typedef [uuid(C1D3A8C0-A4AA-11D0-819C-00A0C90FFFC3)] struct_tagUDT {
      unsigned long a1;
      BSTR pbstr;
   } UDT;
```



The structure, named "UDT", is defined with two data types, an unsigned long and a BSTR.

After you have generated your header file, you must fetch the [**IRecordInfo**](/windows/previous-versions/oaidl/nn-oaidl-irecordinfo?branch=master) interface if you intend to pass a safearray of UDTs . For more information on passing a safearray of UDTs, see [Fetching the IRecordInfo Interface](fetching-the-irecordinfo-interface.md) or [Passing Safearray of UDTs](passing-safearray-of-udts.md).

If you intend to pass a single UDT, see [Passing a Single UDT](passing-a-single-udt.md).

 

 




