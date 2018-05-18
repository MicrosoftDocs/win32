---
Description: 'Maps to the W3C cross origin settings (CORS) attribute used by the HTML5 media element.'
ms.assetid: '77A8F413-5AA8-49E4-9846-A3F87FB878E7'
title: '\_MF\_CROSS\_ORIGIN\_POLICY enumeration'
---

# \_MF\_CROSS\_ORIGIN\_POLICY enumeration

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Maps to the W3C cross origin settings (CORS) attribute used by the HTML5 media element

## Syntax


```C++
typedef enum __MF_CROSS_ORIGIN_POLICY { 
  MF_CROSS_ORIGIN_POLICY_NONE             = 0,
  MF_CROSS_ORIGIN_POLICY_ANONYMOUS        = 1,
  MF_CROSS_ORIGIN_POLICY_USE_CREDENTIALS  = 2
} _MF_CROSS_ORIGIN_POLICY;
```



## Constants

<dl> <dt>

<span id="MF_CROSS_ORIGIN_POLICY_NONE"></span><span id="mf_cross_origin_policy_none"></span>**MF\_CROSS\_ORIGIN\_POLICY\_NONE**
</dt> <dd>

No CORS state.

</dd> <dt>

<span id="MF_CROSS_ORIGIN_POLICY_ANONYMOUS"></span><span id="mf_cross_origin_policy_anonymous"></span>**MF\_CROSS\_ORIGIN\_POLICY\_ANONYMOUS**
</dt> <dd>

Requests for the element will have their mode set to "cors" and their credentials mode set to "same-origin".

</dd> <dt>

<span id="MF_CROSS_ORIGIN_POLICY_USE_CREDENTIALS"></span><span id="mf_cross_origin_policy_use_credentials"></span>**MF\_CROSS\_ORIGIN\_POLICY\_USE\_CREDENTIALS**
</dt> <dd>

Requests for the element will have their mode set to "cors" and their credentials mode set to "include".

</dd> </dl>

 

 



