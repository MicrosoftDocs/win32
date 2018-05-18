---
Description: 'This section contains reference topics for the Ntdef.h header.'
ms.assetid: 'C2D8E3C5-5291-427A-BB12-B0066AC28431'
title: 'Ntdef.h'
---

# Ntdef.h

This section contains reference topics for the Ntdef.h header.

## In this section



| Topic                                                                       | Description                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ANSI\_STRING**](ansi-string.md)<br/>                              | The **ANSI\_STRING** structure defines a counted string used for ANSI strings.<br/>                                                                                                                                                         |
| [**ARGUMENT\_PRESENT**](argument-present.md)<br/>                    | The **ARGUMENT\_PRESENT** macro takes an argument pointer and returns **FALSE** if the pointer is **NULL**. Otherwise, it returns **TRUE**.<br/>                                                                                            |
| [**COMPARTMENT\_ID**](compartment-id.md)<br/>                        | The **COMPARTMENT\_ID** enumeration indicates the network routing compartment identifier.<br/>                                                                                                                                              |
| [**FIELD\_OFFSET**](field-offset.md)<br/>                            | The **FIELD\_OFFSET** macro returns the byte offset of a named field in a known structure type.<br/>                                                                                                                                        |
| [**GROUP\_AFFINITY**](group-affinity.md)<br/>                        | The **GROUP\_AFFINITY** structure specifies a group number and the processor [affinity](wdkgloss.a#wdkgloss-affinity) within that group.<br/>                                                                             |
| [**InitializeObjectAttributes**](initializeobjectattributes.md)<br/> | The **InitializeObjectAttributes** macro initializes the opaque [**OBJECT\_ATTRIBUTES**](object-attributes.md) structure, which specifies the properties of an object handle to routines that open handles.<br/>                           |
| [**LIST\_ENTRY**](list-entry.md)<br/>                                | A **LIST\_ENTRY** structure describes an entry in a doubly linked list or serves as the header for such a list.<br/>                                                                                                                        |
| [**LUID**](luid.md)<br/>                                             | The **LUID** structure is an opaque structure that specifies an identifier that is guaranteed to be unique on the local machine. For more information, see the reference page for **LUID** in the Microsoft Windows SDK documentation.<br/> |
| [**OBJECT\_ATTRIBUTES**](object-attributes.md)<br/>                  | The **OBJECT\_ATTRIBUTES** structure specifies attributes that can be applied to objects or object handles by routines that create objects and/or return handles to objects.<br/>                                                           |
| [**OEM\_STRING**](oem-string.md)<br/>                                | The **OEM\_STRING** structure defines a counted string used for OEM strings.<br/>                                                                                                                                                           |
| [**PROCESSOR\_NUMBER**](processor-number.md)<br/>                    | The **PROCESSOR\_NUMBER** structure identifies a processor by its group number and group-relative processor number.<br/>                                                                                                                    |
| [**SINGLE\_LIST\_ENTRY**](single-list-entry.md)<br/>                 | A **SINGLE\_LIST\_ENTRY** structure describes an entry in a singly linked list, or serves as the header for such a list.<br/>                                                                                                               |
| [**UNICODE\_STRING**](unicode-string.md)<br/>                        | The **UNICODE\_STRING** structure is used to define Unicode strings.<br/>                                                                                                                                                                   |
| [**ZwDuplicateObject**](zwduplicateobject.md)<br/>                   | The **ZwDuplicateObject** routine creates a handle that is a duplicate of the specified source handle.<br/>                                                                                                                                 |
| [**ZwOpenDirectoryObject**](zwopendirectoryobject.md)<br/>           | The **ZwOpenDirectoryObject** routine opens an existing directory object. <br/>                                                                                                                                                             |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Ntdef.h%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




