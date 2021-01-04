---
title: PICTYPE Constants (OleCtl.h)
description: Describe the type of a picture object as returned by IPicture get\_Type, as well as to describe the type of picture in the picType member of the PICTDESC structure that is passed to OleCreatePictureIndirect.
ms.assetid: 79f10687-f0eb-4b5e-a1a9-9186dbd0b51f
topic_type:
- apiref
api_name:
- PICTYPE_UNINITIALIZED
- PICTYPE_NONE
- PICTYPE_BITMAP
- PICTYPE_METAFILE
- PICTYPE_ICON
- PICTYPE_ENHMETAFILE
api_location:
- OleCtl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PICTYPE Constants

Describe the type of a picture object as returned by [**IPicture::get\_Type**](/windows/desktop/api/OCIdl/nf-ocidl-ipicture-get_type), as well as to describe the type of picture in the **picType** member of the [**PICTDESC**](/windows/win32/api/olectl/ns-olectl-pictdesc) structure that is passed to [**OleCreatePictureIndirect**](/windows/desktop/api/OleCtl/nf-olectl-olecreatepictureindirect).



| Constant/value                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                   |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PICTYPE_UNINITIALIZED"></span><span id="pictype_uninitialized"></span><dl> <dt>**PICTYPE\_UNINITIALIZED**</dt> <dt>(-1)</dt> </dl> | The picture object is currently uninitialized. This value is only valid as a return value from [**IPicture::get\_Type**](/windows/desktop/api/OCIdl/nf-ocidl-ipicture-get_type) and is not valid with the [**PICTDESC**](/windows/win32/api/olectl/ns-olectl-pictdesc) structure.<br/>  |
| <span id="PICTYPE_NONE"></span><span id="pictype_none"></span><dl> <dt>**PICTYPE\_NONE**</dt> <dt>0</dt> </dl>                               | A new picture object is to be created without an initialized state. This value is valid only in the [**PICTDESC**](/windows/win32/api/olectl/ns-olectl-pictdesc) structure.<br/>                                                                        |
| <span id="PICTYPE_BITMAP"></span><span id="pictype_bitmap"></span><dl> <dt>**PICTYPE\_BITMAP**</dt> <dt>1</dt> </dl>                         | The picture type is a bitmap. When this value occurs in the [**PICTDESC**](/windows/win32/api/olectl/ns-olectl-pictdesc) structure, it means that the **bmp** field of that structure contains the relevant initialization parameters.<br/>             |
| <span id="PICTYPE_METAFILE"></span><span id="pictype_metafile"></span><dl> <dt>**PICTYPE\_METAFILE**</dt> <dt>2</dt> </dl>                   | The picture type is a metafile. When this value occurs in the [**PICTDESC**](/windows/win32/api/olectl/ns-olectl-pictdesc) structure, it means that the **wmf** field of that structure contains the relevant initialization parameters.<br/>           |
| <span id="PICTYPE_ICON"></span><span id="pictype_icon"></span><dl> <dt>**PICTYPE\_ICON**</dt> <dt>3</dt> </dl>                               | The picture type is an icon. When this value occurs in the [**PICTDESC**](/windows/win32/api/olectl/ns-olectl-pictdesc) structure, it means that the **icon** field of that structure contains the relevant initialization parameters.<br/>             |
| <span id="PICTYPE_ENHMETAFILE"></span><span id="pictype_enhmetafile"></span><dl> <dt>**PICTYPE\_ENHMETAFILE**</dt> <dt>4</dt> </dl>          | The picture type is an enhanced metafile. When this value occurs in the [**PICTDESC**](/windows/win32/api/olectl/ns-olectl-pictdesc) structure, it means that the **emf** field of that structure contains the relevant initialization parameters.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>OleCtl.h</dt> </dl> |



## See also

<dl> <dt>

[**IPicture::get\_Type**](/windows/desktop/api/OCIdl/nf-ocidl-ipicture-get_type)
</dt> <dt>

[**OleCreatePictureIndirect**](/windows/desktop/api/OleCtl/nf-olectl-olecreatepictureindirect)
</dt> <dt>

[**PICTDESC**](/windows/win32/api/olectl/ns-olectl-pictdesc)
</dt> </dl>

 

 





