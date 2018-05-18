---
Description: Checking Role Membership
ms.assetid: '690cab3f-4476-4fce-b842-d63a4d0d5c6f'
title: Checking Role Membership
---

# Checking Role Membership

You can call the [**ISecurityCallContext::IsCallerInRole**](isecuritycallcontext-iscallerinrole.md) method to determine whether an object's direct caller is a member of a particular role. This functionality is useful when you want to ensure that a certain block of code is not executed unless the caller is a member of a particular role.

For example, you could use [**IsCallerInRole**](isecuritycallcontext-iscallerinrole.md) to ensure that transactions over a specified amount, such as $1000, are performed only by members of a Managers role. If the caller is not a Manager and the transaction is over $1000, the transaction is not performed and an error message is displayed.

The preferred way to access [**IsCallerInRole**](isecuritycallcontext-iscallerinrole.md) is through the security call context object because you can use the same reference to the security call context object to obtain security properties. However, you can also access the **IsCallerInRole**method from the **ObjectContext** object. (See [**ObjectContext**](objectcontext.md) or [**IObjectContext**](iobjectcontext.md) for more information.)

If you are developing components for a Microsoft Visual Basic application, you call the [**GetSecurityCallContext**](igetsecuritycallcontext-getsecuritycallcontext.md) function and then use the security call context to call [**IsCallerInRole**](isecuritycallcontext-iscallerinrole.md), as shown in the following example:


```VB
If (GetSecurityCallContext.IsCallerInRole("Manager")) Then
   ' Go ahead and perform the transaction.
Else
   ' Display an error message.
End If
```



If you are developing a C or C++ application, use [**CoGetCallContext**](https://msdn.microsoft.com/library/windows/desktop/ms691483) to retrieve a pointer to the [**ISecurityCallContext**](isecuritycallcontext.md) interface. Then you call [**ISecurityCallContext::IsCallerInRole**](isecuritycallcontext-iscallerinrole.md), as shown in the following example:


```C++
ISecurityCallContext* pSecCtx;
VARIANT_BOOL bIsInRole;

HRESULT hr = CoGetCallContext(IID_ISecurityCallContext, (void**)&amp;pSecCtx);
if (FAILED(hr)) throw(hr);
if (NULL == pSecCtx) { 
    // No security call context is available.
    // Display an error message and return.
    return E_FAIL;
}
hr = pSecCtx->IsCallerInRole(myRole, &amp;bIsInRole);
return hr;
```



## Related topics

<dl> <dt>

[Accessing Security Call Context Information](accessing-security-call-context-information.md)
</dt> <dt>

[Determining Whether Role-Based Security Is Enabled](determining-whether-role-based-security-is-enabled.md)
</dt> <dt>

[Programmatic Component Security](programmatic-component-security.md)
</dt> </dl>

 

 



