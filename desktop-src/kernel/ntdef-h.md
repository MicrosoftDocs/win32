---
Description: This section contains reference topics for the Ntdef.h header.
ms.assetid: C2D8E3C5-5291-427A-BB12-B0066AC28431
title: Ntdef.h
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ntdef.h

This section contains reference topics for the Ntdef.h header.

## In this section



| Topic                                                                       | Description                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ANSI\_STRING**](/windows/desktop/api/Ntdef/ns-ntdef-_string)<br/>                              | The **ANSI\_STRING** structure defines a counted string used for ANSI strings.<br/>                                                                                                                                                         |
| [**ARGUMENT\_PRESENT**](/windows-hardware/drivers/ddi/content/wudfwdm/nf-wudfwdm-argument_present)<br/>                    | The **ARGUMENT\_PRESENT** macro takes an argument pointer and returns **FALSE** if the pointer is **NULL**. Otherwise, it returns **TRUE**.<br/>                                                                                            |
| [**COMPARTMENT\_ID**](/windows/desktop/api/ntdef/ne-ntdef-compartment_id)<br/>                        | The **COMPARTMENT\_ID** enumeration indicates the network routing compartment identifier.<br/>                                                                                                                                              |
| [**FIELD\_OFFSET**](/windows/desktop/api/ntdef/nf-ntdef-field_offset)<br/>                            | The **FIELD\_OFFSET** macro returns the byte offset of a named field in a known structure type.<br/>                                                                                                                                        |
| [**GROUP\_AFFINITY**](/windows-hardware/drivers/ddi/content/miniport/ns-miniport-_group_affinity)<br/>                        | The **GROUP\_AFFINITY** structure specifies a group number and the processor [affinity](https://www.bing.com/search?q=affinity) within that group.<br/>                                                                             |
| [**InitializeObjectAttributes**](/windows-hardware/drivers/ddi/content/wudfwdm/nf-wudfwdm-initializeobjectattributes)<br/> | The **InitializeObjectAttributes** macro initializes the opaque [**OBJECT\_ATTRIBUTES**](/windows-hardware/drivers/ddi/content/wudfwdm/ns-wudfwdm-_object_attributes) structure, which specifies the properties of an object handle to routines that open handles.<br/>                           |
| [**LIST\_ENTRY**](/windows/desktop/api/Ntdef/ns-ntdef-_list_entry)<br/>                                | A **LIST\_ENTRY** structure describes an entry in a doubly linked list or serves as the header for such a list.<br/>                                                                                                                        |
| [**LUID**](/windows/desktop/api/Ntdef/ns-ntdef-_luid)<br/>                                             | The **LUID** structure is an opaque structure that specifies an identifier that is guaranteed to be unique on the local machine. For more information, see the reference page for **LUID** in the Microsoft Windows SDK documentation.<br/> |
| [**OBJECT\_ATTRIBUTES**](/windows-hardware/drivers/ddi/content/wudfwdm/ns-wudfwdm-_object_attributes)<br/>                  | The **OBJECT\_ATTRIBUTES** structure specifies attributes that can be applied to objects or object handles by routines that create objects and/or return handles to objects.<br/>                                                           |
| [**OEM\_STRING**](/windows/desktop/api/Ntdef/)<br/>                                | The **OEM\_STRING** structure defines a counted string used for OEM strings.<br/>                                                                                                                                                           |
| [**PROCESSOR\_NUMBER**](/windows-hardware/drivers/ddi/content/miniport/ns-miniport-_processor_number)<br/>                    | The **PROCESSOR\_NUMBER** structure identifies a processor by its group number and group-relative processor number.<br/>                                                                                                                    |
| [**SINGLE\_LIST\_ENTRY**](/windows/desktop/api/ntdef/ns-ntdef-_single_list_entry)<br/>                 | A **SINGLE\_LIST\_ENTRY** structure describes an entry in a singly linked list, or serves as the header for such a list.<br/>                                                                                                               |
| [**UNICODE\_STRING**](/windows-hardware/drivers/ddi/content/wudfwdm/ns-wudfwdm-_unicode_string)<br/>                        | The **UNICODE\_STRING** structure is used to define Unicode strings.<br/>                                                                                                                                                                   |
| [**ZwDuplicateObject**](/windows-hardware/drivers/ddi/content/Ntifs/nf-ntifs-zwduplicateobject)<br/>                   | The **ZwDuplicateObject** routine creates a handle that is a duplicate of the specified source handle.<br/>                                                                                                                                 |
| [**ZwOpenDirectoryObject**](/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-zwopendirectoryobject)<br/>           | The **ZwOpenDirectoryObject** routine opens an existing directory object. <br/>                                                                                                                                                             |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Ntdef.h%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




