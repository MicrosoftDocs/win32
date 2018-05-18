---
title: Passing UDTs
description: To pass single UDTs or safearrays of UDTs through type-library driven marshaling for v-table binding, C and C++ Automation clients need the header file generated from the IDL that describes the UDT.
ms.assetid: 'a9b968e9-2241-4d99-9e59-6ee0aeea5942'
---

# Passing UDTs

To pass single UDTs or safearrays of UDTs through type-library driven marshaling for v-table binding, C and C++ Automation clients need the header file generated from the IDL that describes the UDT. Visual Basic clients require the type library generated from the IDL file.

To pass single UDTs or safearrays of UDTs for late binding, the Automation client must have the information necessary to store the type information of the UDT into a VARIANT (and if late-binding, the UDT must be self-described). A VARIANT of type VT\_RECORD wraps a RecordInfo object, which contains the necessary information about the UDT and a pointer the UDT itself. The RecordInfo object implements a new interface, [**IRecordInfo**](irecordinfo.md), for access to the information. It is important to know that the actual storage of the UDT is never owned by the VARIANT; the **IRecordInfo** pointer is the only thing that is owned by the VARIANT.

The data for a UDT includes an [**IRecordInfo**](irecordinfo.md) pointer to the description of the UDT, *pRecInfo*, and a pointer to the data, *pvRecord*.

To pass a UDT or safearray of UDTs in v-table binding, the Automation client is configured by following these steps:

1.  For Visual Basic the client needs the type library generated from the server's IDL file, which describes the data types of the UDT. For C and C++ the client needs the header file generated from the server's IDL file , or to import the type library using the \#import directive. For more information, see [Describing UDT in the IDL File](describing-udt-in-the-idl-file.md).

2.  For passing a safearray of UDTs in Visual Basic, the client will need to fetch the [**IRecordInfo**](irecordinfo.md) interface from the type library for specifying the type information of the UDT.

    For more information on how to fetch the [**IRecordInfo**](irecordinfo.md) interface for v-table binding and late binding see [Fetching the IRecordInfo Interface](fetching-the-irecordinfo-interface.md).

3.  The client and server will then simply declare the UDT as one does any native Automation type and passes it to the other. The client calls the method.

For more information on how to pass a single UDT, see [Passing a Single UDT](passing-a-single-udt.md).

For more information on how to pass a safearray of UDTs, see [Passing Safearray of UDTs](55A1EFFB-067F-4AE7-9E88-BCCBFD7DA433).

## Related topics

<dl> <dt>

[**IRecordInfo**](irecordinfo.md)
</dt> </dl>

 

 




