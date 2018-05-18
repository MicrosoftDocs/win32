---
Description: 'Determining Whether Role-Based Security Is Enabled'
ms.assetid: 'b5e6ab7e-5a77-4c6f-9bec-02942bba389d'
title: 'Determining Whether Role-Based Security Is Enabled'
---

# Determining Whether Role-Based Security Is Enabled

By using the [**ISecurityCallContext::IsSecurityEnabled**](isecuritycallcontext-issecurityenabled.md) method available from the security call context object, you can determine whether security is enabled for the current object. You should call **IsSecurityEnabled** before you use ISecurityCallContext::[**IsCallerInRole**](isecuritycallcontext-iscallerinrole.md) to check role membership because **IsCallerInRole** returns True if security is not enabled.

Microsoft Visual Basic developers call [**GetSecurityCallContext**](igetsecuritycallcontext-getsecuritycallcontext.md) to obtain a reference to a [**SecurityCallContext**](securitycallcontext.md) object and then call [**IsSecurityEnabled**](isecuritycallcontext-issecurityenabled.md), as shown in the following example:


```VB
Dim objSecCallCtx As SecurityCallContext
Dim boolSecEn As Boolean
Set objSecCallCtx = GetSecurityCallContext()
boolSecEn = objSecCallCtx.IsSecurityEnabled()
 
```



Microsoft Visual C++ developers can call [**ISecurityCallContext::IsSecurityEnabled**](isecuritycallcontext-issecurityenabled.md) by calling [**CoGetCallContext**](https://msdn.microsoft.com/library/windows/desktop/ms691483) to obtain a pointer to [**ISecurityCallContext**](isecuritycallcontext.md) and then calling **IsSecurityEnabled**. A brief example follows:


```C++
ISecurityCallContext* pSecCtx;
VARIANT_BOOL bIsEnabled;

HRESULT hr1 = CoGetCallContext(IID_ISecurityCallContext, (void**)&amp;pSecCtx);
if (FAILED(hr1)) throw(hr1);
if (NULL == pSecCtx) {
    // Display error message.
    return E_FAIL;
}

HRESULT hr2 = pSecCtx->IsSecurityEnabled(&amp;bIsEnabled);
return hr2;
```



Although the preferred way to call [**IsSecurityEnabled**](isecuritycallcontext-issecurityenabled.md) is by using the security call context object, you can also call **IsSecurityEnabled** through the object context. (See [**ObjectContext**](objectcontext.md) or [**IObjectContext**](iobjectcontext.md) for more information.)

## Related topics

<dl> <dt>

[Accessing Security Call Context Information](accessing-security-call-context-information.md)
</dt> <dt>

[Checking Role Membership](checking-role-membership.md)
</dt> <dt>

[Programmatic Component Security](programmatic-component-security.md)
</dt> </dl>

 

 



