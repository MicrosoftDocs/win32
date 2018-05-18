---
Description: 'The PF\_FOLLOWENTRY structure defines a protocol that Network Monitor adds to the follow set of a parser.'
ms.assetid: '931ae70f-8c5e-4b7a-aae6-64a33dac3b23'
title: 'PF\_FOLLOWENTRY structure'
---

# PF\_FOLLOWENTRY structure

The **PF\_FOLLOWENTRY** structure defines a protocol that Network Monitor adds to the follow set of a parser.

## Syntax


```C++
typedef struct _PF_FOLLOWENTRY {
  char szProtocol[MAX_PROTOCOL_NAME_LEN];
} PF_FOLLOWENTRY, *PPF_FOLLOWENTRY;
```



## Members

<dl> <dt>

**szProtocol**
</dt> <dd>

The name of the protocol.

</dd> </dl>

## Remarks

The [PF\_FOLLOWSET](pf-followset.md) structure uses an array of **PF\_FOLLOWENTRY** structures.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[PF\_FOLLOWSET](pf-followset.md)
</dt> </dl>

 

 




