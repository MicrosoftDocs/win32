---
title: Binding to Child Objects
description: In ADSI, a container object exposes the IADsContainer interface.
ms.assetid: 16b913ea-06a4-4e85-ad6c-68817883bbd8
ms.tgt_platform: multiple
keywords:
- ADSI ADSI , using, binding to child objects
- Binding to Child Objects
- Child Objects, Binding to
ms.topic: article
ms.date: 05/31/2018
---

# Binding to Child Objects

In ADSI, a container object exposes the [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer) interface. The [**IADsContainer::GetObject**](/windows/desktop/api/Iads/nf-iads-iadscontainer-getobject) method is used to bind directly to a child object. The object returned by **IADsContainer::GetObject** has the same security context as the object on which the method was called. This means that if alternate credentials are used, the alternate credentials do not have to be passed to the binding function or method again to maintain the same credentials.

The [**IADsContainer::GetObject**](/windows/desktop/api/Iads/nf-iads-iadscontainer-getobject) method takes a relative distinguished name (RDN) that is relative to the current object. This method also takes an optional class name and returns an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface pointer that represents the child object. To obtain the desired ADSI interface, such as [**IADs**](/windows/desktop/api/Iads/nn-iads-iads), call the [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) method of this **IDispatch** interface pointer.

The following C++ code example shows a function that retrieves a specified child object.


```C++
HRESULT GetChildObject(IADs *pObject, 
                       LPCWSTR pwszClass, 
                       LPCWSTR pwszRDN, 
                       IADs **ppChild)
{
    if(NULL == ppChild)
    {
        return E_INVALIDARG;
    }

    *ppChild = NULL;
    
    if((NULL == pObject) || (NULL == pwszRDN))
    {
        return E_INVALIDARG;
    }

    HRESULT hr;
    IADsContainer *pCont;

    hr = pObject->QueryInterface(IID_IADsContainer, (LPVOID*)&pCont);
    if(SUCCEEDED(hr))
    {
        BSTR bstrClass = NULL;
        if(pwszClass)
        {
            bstrClass = SysAllocString(pwszClass);
        }

        BSTR bstrRDN = SysAllocString(pwszRDN);
        if(bstrRDN)
        {
            IDispatch *pDisp;
            
            hr = pCont->GetObject(bstrClass, bstrRDN, &pDisp);
            if(SUCCEEDED(hr))
            {
                hr = pDisp->QueryInterface(IID_IADs, (LPVOID*)ppChild);
                
                pDisp->Release();
            }

        }
        else
        {
            hr = E_OUTOFMEMORY;
        }

        if(bstrRDN)
        {
            SysFreeString(bstrRDN);
        }

        if(bstrClass)
        {
            SysFreeString(bstrClass);
        }


        pCont->Release();
    }
    
    return hr;
}
```



 

 