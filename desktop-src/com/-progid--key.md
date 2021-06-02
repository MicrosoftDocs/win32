---
title: ProgID Key
description: A programmatic identifier (ProgID) is a registry entry that can be associated with a CLSID. Like the CLSID, the ProgID identifies a class but with less precision because it is not guaranteed to be globally unique.
ms.assetid: f9ef2934-0815-4a6f-9283-8f748eee083b
ms.topic: article
ms.date: 05/31/2018
---

# ProgID Key

A programmatic identifier (ProgID) is a registry entry that can be associated with a CLSID. Like the CLSID, the ProgID identifies a class but with less precision because it is not guaranteed to be globally unique.

## Registry Entry

**HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes**\\*{*ProgID*}*



| Registry key                            | Description                                                        |
|-----------------------------------------|--------------------------------------------------------------------|
| [**CLSID**](clsid.md)                  | Associates a ProgID with a CLSID.                                  |
| [**Insertable**](insertable-progid.md) | Indicates that this class is insertable in OLE 2 containers.       |
| [**Protocol**](protocol.md)            | Indicates that this OLE 2 class is insertable in OLE 1 containers. |
| [**Shell**](shell.md)                  | Provides Windows 3.1 shell printing and **File Open** information. |



 

## Remarks

You can use a ProgID in programming situations where it is not possible to use a CLSID. ProgIDs should not appear in the user interface. ProgIDs are not guaranteed to be unique, so they can be used only where name collisions are manageable.

The format of a ProgID is <*Program*>.<*Component*>.<*Version*>, separated by periods and with no spaces, as in Word.Document.6. The ProgID must comply with the following requirements:

-   Have no more than 39 characters.
-   Contain no punctuation (including underscores) except one or more periods.
-   Not start with a digit.
-   Be different from the class name of any OLE 1 application, including the OLE 1 version of the same application, if there is one.

Because the ProgID should not appear in the user interface, you can obtain a displayable name by calling [**IOleObject::GetUserType**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getusertype). Also, see [**OleRegGetUserType**](/windows/desktop/api/Ole2/nf-ole2-olereggetusertype).

The **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Classes** key corresponds to the **HKEY\_CLASSES\_ROOT** key, which was retained for compatibility with earlier versions of COM.

## Related topics

<dl> <dt>

[**IOleObject::GetUserType**](/windows/desktop/api/OleIdl/nf-oleidl-ioleobject-getusertype)
</dt> <dt>

[**OleRegGetUserType**](/windows/desktop/api/Ole2/nf-ole2-olereggetusertype)
</dt> </dl>

 

 




