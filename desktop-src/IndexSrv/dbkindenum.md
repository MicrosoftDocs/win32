---
Description: The DBKINDENUM enumerated type specifies the combination of GUID, property number, or property name to use to identify a database object.
ms.assetid: 05e99f09-fa67-4ad2-9ce1-ace886710616
title: DBKINDENUM enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# DBKINDENUM enumeration

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

The **DBKINDENUM** enumerated type specifies the combination of GUID, property number, or property name to use to identify a database object.

## Syntax


```C++
enum DBKINDENUM {
  DBKIND_GUID_NAME, 
  DBKIND_GUID_PROPID, 
  DBKIND_NAME, 
  DBKIND_PGUID_NAME, 
  DBKIND_PGUID_PROPID, 
  DBKIND_PROPID, 
  DBKIND_GUID 

};
```



## Constants

<dl> <dt>

<span id="DBKIND_GUID_NAME"></span><span id="dbkind_guid_name"></span>**DBKIND\_GUID\_NAME**
</dt> <dd></dd> <dt>

<span id="DBKIND_GUID_PROPID"></span><span id="dbkind_guid_propid"></span>**DBKIND\_GUID\_PROPID**
</dt> <dd></dd> <dt>

<span id="DBKIND_NAME"></span><span id="dbkind_name"></span>**DBKIND\_NAME**
</dt> <dd></dd> <dt>

<span id="DBKIND_PGUID_NAME"></span><span id="dbkind_pguid_name"></span>**DBKIND\_PGUID\_NAME**
</dt> <dd></dd> <dt>

<span id="DBKIND_PGUID_PROPID"></span><span id="dbkind_pguid_propid"></span>**DBKIND\_PGUID\_PROPID**
</dt> <dd></dd> <dt>

<span id="DBKIND_PROPID"></span><span id="dbkind_propid"></span>**DBKIND\_PROPID**
</dt> <dd></dd> <dt>

<span id="DBKIND_GUID"></span><span id="dbkind_guid"></span>**DBKIND\_GUID**
</dt> <dd></dd> </dl>

``` syntax
enum DBKINDENUM {
  DBKIND_GUID_NAME    = 0,                        // use the guid and pwszName members
  DBKIND_GUID_PROPID  = DBKIND_GUID_NAME + 1,     // use the guid and ulPropid members
  DBKIND_NAME         = DBKIND_GUID_PROPID + 1,   // use only the pwszName member, and
                                                  // ignore the uGuid member
  DBKIND_PGUID_NAME   = DBKIND_NAME + 1,          // use the pGuid and pwszName members
  DBKIND_PGUID_PROPID = DBKIND_PGUID_NAME + 1,    // use the pGuid and ulPropid members
  DBKIND_PROPID       = DBKIND_PGUID_PROPID + 1,  // use only the ulPropid member, and
                                                  //  ignore the uGuid member
  DBKIND_GUID         = DBKIND_PROPID + 1         // use only the guid member
};
```

### Remarks

The [**DBID**](dbid.md) structure uses a value from this enumerated type as a parameter.

The OLE DB Provider for Indexing Service accepts only the DBKIND\_GUID\_NAME, DBKIND\_GUID\_PROPID, DBKIND\_PGUID\_NAME, and DBKIND\_PGUID\_PROPID values.

## Requirements



|                                     |                                                            |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |
| End of client support<br/>    | Windows 7<br/>                                       |
| End of server support<br/>    | Windows Server 2008 R2<br/>                          |



 

 




