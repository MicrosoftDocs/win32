---
title: NNTPSTATE enumeration
description: These are the various states the NNTP Transport can be in.
ms.assetid: 'adfaa0de-4bae-4560-9fa4-9da73f793ea7'
keywords: ["NNTPSTATE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# NNTPSTATE enumeration

\[**NNTPSTATE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

These are the various states the NNTP Transport can be in. These states are also used to determine which type of data is being returned in the client's [**OnResponse**](oe-inntpcallback-onresponse.md) callback.

## Syntax


```C++
typedef enum tagNNTPSTATE { 
  NS_DISCONNECTED  = 0,
  NS_CONNECT       = 1,
  NS_AUTHINFO      = 2,
  NS_POST          = 3,
  NS_IDLE          = 4,
  NS_LIST          = 5,
  NS_LISTGROUP     = 6,
  NS_NEWGROUPS     = 7,
  NS_GROUP         = 8,
  NS_LAST          = 9,
  NS_NEXT          = 10,
  NS_STAT          = 11,
  NS_ARTICLE       = 12,
  NS_HEAD          = 13,
  NS_BODY          = 14,
  NS_DATE          = 15,
  NS_MODE          = 16,
  NS_QUIT          = 17,
  NS_HEADERS       = 18,
  NS_XHDR          = 19
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="NS_DISCONNECTED"></span><span id="ns_disconnected"></span>**NS\_DISCONNECTED**
</dt> <dd>

not connected

</dd> <dt>

<span id="NS_CONNECT"></span><span id="ns_connect"></span>**NS\_CONNECT**
</dt> <dd>

awaiting connect response

</dd> <dt>

<span id="NS_AUTHINFO"></span><span id="ns_authinfo"></span>**NS\_AUTHINFO**
</dt> <dd>

awaiting authorization

</dd> <dt>

<span id="NS_POST"></span><span id="ns_post"></span>**NS\_POST**
</dt> <dd>

awaiting CommandPOST() to complete

</dd> <dt>

<span id="NS_IDLE"></span><span id="ns_idle"></span>**NS\_IDLE**
</dt> <dd>

connected (and authorized if necessary)

</dd> <dt>

<span id="NS_LIST"></span><span id="ns_list"></span>**NS\_LIST**
</dt> <dd>

awaiting LIST data

</dd> <dt>

<span id="NS_LISTGROUP"></span><span id="ns_listgroup"></span>**NS\_LISTGROUP**
</dt> <dd>

awaiting LISTGROUP data

</dd> <dt>

<span id="NS_NEWGROUPS"></span><span id="ns_newgroups"></span>**NS\_NEWGROUPS**
</dt> <dd>

awaiting NEWGROUPS data

</dd> <dt>

<span id="NS_GROUP"></span><span id="ns_group"></span>**NS\_GROUP**
</dt> <dd>

awaiting GROUP response

</dd> <dt>

<span id="NS_LAST"></span><span id="ns_last"></span>**NS\_LAST**
</dt> <dd>

awaiting LAST response

</dd> <dt>

<span id="NS_NEXT"></span><span id="ns_next"></span>**NS\_NEXT**
</dt> <dd>

awaiting NEXT response

</dd> <dt>

<span id="NS_STAT"></span><span id="ns_stat"></span>**NS\_STAT**
</dt> <dd>

awaiting STAT response

</dd> <dt>

<span id="NS_ARTICLE"></span><span id="ns_article"></span>**NS\_ARTICLE**
</dt> <dd>

awaiting ARTICLE data

</dd> <dt>

<span id="NS_HEAD"></span><span id="ns_head"></span>**NS\_HEAD**
</dt> <dd>

awaiting HEAD data

</dd> <dt>

<span id="NS_BODY"></span><span id="ns_body"></span>**NS\_BODY**
</dt> <dd>

awaiting BODY data

</dd> <dt>

<span id="NS_DATE"></span><span id="ns_date"></span>**NS\_DATE**
</dt> <dd>

awaiting DATE response

</dd> <dt>

<span id="NS_MODE"></span><span id="ns_mode"></span>**NS\_MODE**
</dt> <dd>

awaiting MODE response

</dd> <dt>

<span id="NS_QUIT"></span><span id="ns_quit"></span>**NS\_QUIT**
</dt> <dd>

awaiting QUIT response

</dd> <dt>

<span id="NS_HEADERS"></span><span id="ns_headers"></span>**NS\_HEADERS**
</dt> <dd>

awaiting XOVER or XHDR data from [**GetHeaders**](oe-inntptransport-getheaders.md)

</dd> <dt>

<span id="NS_XHDR"></span><span id="ns_xhdr"></span>**NS\_XHDR**
</dt> <dd>

awaiting XHDR data

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





