---
description: Contains DDE share attributes maintained by the NetDDE Share Database Manager (DSDM).
ms.assetid: f4101553-06ef-4f83-87c7-5b6fdf0467e5
title: NDDESHAREINFO structure (Nddeapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NDDESHAREINFO
api_type: 
- HeaderDef
api_location: 
- Nddeapi.h
---

# NDDESHAREINFO structure

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Contains DDE share attributes maintained by the NetDDE Share Database Manager (DSDM). The security descriptor associated with each DDE share is not passed through this structure but is accessed through specific functions. The NetDDE DSDM API accepts this structure for set functions; for get functions, the DSDM returns the structure packed into the supplied buffer along with the data referenced by the members **lpszShareName**, **lpszAppTopicList**, and **lpszItemList**.

## Syntax


```C++
typedef struct _NDDESHAREINFO {
  LONG   lRevision;
  LPTSTR lpszShareName;
  LONG   lShareType;
  LPTSTR lpszAppTopicList;
  LONG   fSharedFlag;
  LONG   fService;
  LONG   fStartAppFlag;
  LONG   nCmdShow;
  LONG   qModifyId[2];
  LONG   cNumItems;
  LPTSTR lpszItemList;
} NDDESHAREINFO, *PNDDESHAREINFO;
```



## Members

<dl> <dt>

**lRevision**
</dt> <dd>

The revision level of the **NDDESHAREINFO** structure. Currently, the revision level is 1.

</dd> <dt>

**lpszShareName**
</dt> <dd>

The name of the share. This string must be no more than MAX\_NDDESHARENAME characters long.

</dd> <dt>

**lShareType**
</dt> <dd>

One or more DDE share types. This member can be a combination of the following supported DDE share types.



| Share type                                                                                                                                                                                                                           | Meaning                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="SHARE_TYPE_NEW"></span><span id="share_type_new"></span><dl> <dt>**SHARE\_TYPE\_NEW**</dt> <dt>0x02</dt> </dl>          | The share contains an OLE application/topic pair.<br/>   |
| <span id="SHARE_TYPE_OLD"></span><span id="share_type_old"></span><dl> <dt>**SHARE\_TYPE\_OLD**</dt> <dt>0x01</dt> </dl>          | The share contains a DDE application/topic pair.<br/>    |
| <span id="SHARE_TYPE_STATIC"></span><span id="share_type_static"></span><dl> <dt>**SHARE\_TYPE\_STATIC**</dt> <dt>0x04</dt> </dl> | The share contains a static application/topic pair.<br/> |



 

</dd> <dt>

**lpszAppTopicList**
</dt> <dd>

A pointer to a buffer containing null-terminated strings for the DDE, OLE, and static application/topic pairs. The buffer should be in the following format:

``` syntax
<DDE application name>|<DDE topic name>\0
<OLE application name>|<OLE topic name>\0
<static application name>|<static topic name>\0\0
```

</dd> <dt>

**fSharedFlag**
</dt> <dd>

If this member is **FALSE**, the DDE share will not allow remote users to communicate through it by using DDE. However, local users can still communicate through the DDE share. Local client links are always implied if the associated DACL grants access.

</dd> <dt>

**fService**
</dt> <dd>

If this member is set, the DDE share will not check whether the current user has set it as trusted before allowing DDE communication.

</dd> <dt>

**fStartAppFlag**
</dt> <dd>

If this member is set and the share is trusted to start applications, NetDDE will attempt to start the application specified by **lpszAppTopicList** if it cannot initially start a DDE conversation with the application.

</dd> <dt>

**nCmdShow**
</dt> <dd>

When NetDDE starts an application to initiate a DDE conversation, this value is sent to the application through the *nCmdShow* parameter of the [**WinMain**](/windows/win32/api/winbase/nf-winbase-winmain) function. It defines the preferred mode for the application window to be shown in. This parameter is significant only if **fStartAppFlag** is active. The logged on user in whose context the application is started can also override this option when promoting the share to trusted status. The default for this member is SW\_SHOWMAXIMIZED.

</dd> <dt>

**qModifyId**
</dt> <dd>

An 8-byte serial number that indicates the modification serial number of the DDE share. Every time the DDE share is modified by a [**NDdeShareSetInfo**](nddesharesetinfo.md) or [**NDdeSetShareSecurity**](nddesetsharesecurity.md) call, these values are changed.

</dd> <dt>

**cNumItems**
</dt> <dd>

The number of items listed in **lpszItemList**. If **cNumItems** is zero, then **lpszItemList** is empty, and the share information and associated security descriptor apply to all items serviced by the associated application.

</dd> <dt>

**lpszItemList**
</dt> <dd>

A pointer to a buffer containing null-terminated strings that specify the items the client application in a DDE transaction can request or start advise loops on. If no items are listed, the DDE share allows any item to be used. The number of items in the list must match the **cNumItems** count.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Nddeapi.h</dt> </dl> |



## See also

<dl> <dt>

[Network Dynamic Data Exchange Overview](network-dynamic-data-exchange.md)
</dt> <dt>

[Network DDE Structures](network-dde-structures.md)
</dt> <dt>

[**NDdeSetShareSecurity**](nddesetsharesecurity.md)
</dt> <dt>

[**NDdeShareSetInfo**](nddesharesetinfo.md)
</dt> <dt>

[**WinMain**](/windows/win32/api/winbase/nf-winbase-winmain)
</dt> </dl>

 

