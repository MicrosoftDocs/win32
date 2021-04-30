---
title: add urlacl
description: Reserves the specified URL for non-administrator users and accounts.
ms.assetid: 5d89dec3-26e6-4db8-b4cc-e9b933ac60c5
keywords:
- add urlacl HTTP
topic_type:
- apiref
api_name:
- add urlacl
api_type:
- NA
ms.topic: reference
ms.custom: snippet-project
ms.date: 07/29/2020
---

# add urlacl

Reserves the specified URL for non-administrator users and accounts. The discretionary access control list (DACL) can be specified by using an account name with the listen and delegate parameters or by using a security descriptor definition language (SDDL) string.

``` syntax
add urlacl [url=]string
           [[user=]string
           {[[listen={yes|no}] [delegate={yes|no}]] | [sddl=]string}

 
```

## Parameters

<dl> <dt>

<span id="_url__string"></span><span id="_URL__STRING"></span>
**[url=] string**
</dt> <dd>

Specifies the fully qualified URL.

</dd> <dt>

<span id="_user__string"></span><span id="_USER__STRING"></span>
**[user=] string**
</dt> <dd>

Specifies the user or user group name.

</dd> <dt>

<span id="_listen__yes_no__"></span><span id="_LISTEN__YES_NO__"></span>**\[listen={yes\|no}\]**
</dt> <dd>

Specifies one of the following values:

-   yes: Allows the user to register URLs. This is the default value.
-   no: Denies the user from registering URLs.

</dd> <dt>

<span id="_delegate__yes_no__"></span><span id="_DELEGATE__YES_NO__"></span>**\[delegate={yes\|no}\]**
</dt> <dd>

Specifies one of the following values:

-   yes: Allows the user to delegate URLs.
-   no: Denies the user from delegating URLs. This is the default value.

</dd> <dt>

<span id="_sddl__string"></span><span id="_SDDL__STRING"></span>
**[sddl=] string**
</dt> <dd>

Specifies the SDDL string that describes the DACL.

</dd> </dl>

## Examples

* add urlacl url=https://+:80/MyUri user=DOMAIN\\user

* add urlacl url=https://www.contoso.com:80/MyUri user=DOMAIN\\user listen=yes

* add urlacl url=https://www.contoso.com:80/MyUri user=DOMAIN\\user delegate=no

 
## See Also

* [Netsh http commands](/windows-server/networking/technologies/netsh/netsh-http#add-urlacl)
 