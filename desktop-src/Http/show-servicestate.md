---
title: show servicestate
description: Shows a snapshot of the HTTP service.
ms.assetid: 'a50a3ef5-5e62-412e-a443-11d453778f70'
keywords: ["show servicestate HTTP"]
topic_type:
- apiref
api_name:
- show servicestate
api_type:
- NA
---

# show servicestate

Shows a snapshot of the HTTP service.

``` syntax
show servicestate [[view=]{session|requestq}] [[verbose=]{yes|no}]
 
```

## Parameters

<dl> <dt>

<span id="__view___session_requestq__"></span><span id="__VIEW___SESSION_REQUESTQ__"></span>**\[\[view=\]{session\|requestq}\]**
</dt> <dd>

View snapshot of HTTP service state based on server session or request queues.

</dd> <dt>

<span id="__verbose___yes_no__"></span><span id="__VERBOSE___YES_NO__"></span>**\[\[verbose=\]{yes\|no}\]**
</dt> <dd>

View verbose information showing property information too.

</dd> </dl>

## Examples

**show servicestate view=session**

**show servicestate view=requestq verbose=yes**

 

 




