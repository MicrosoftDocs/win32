---
description: The INonDelegatingUnknown interface is a version of IUnknown that is renamed to enable support for both nondelegating and delegating IUnknown interfaces in the same COM object.
ms.assetid: a2faf9d1-2130-4c6c-8fcd-3e118d592b7f
title: INonDelegatingUnknown (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- INonDelegatingUnknown
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# INonDelegatingUnknown

The `INonDelegatingUnknown` interface is a version of **IUnknown** that is renamed to enable support for both nondelegating and delegating **IUnknown** interfaces in the same COM object.

## Syntax


```C++
interface INonDelegatingUnknown
{
    virtual HRESULT NonDelegatingQueryInterface) (REFIID riid, LPVOID *ppv) PURE;
    virtual ULONG NonDelegatingAddRef)(void) PURE;
    virtual ULONG NonDelegatingRelease)(void) PURE;
};
```



## Remarks

To use `INonDelegatingUnknown` for multiple inheritance, perform the following steps.

1.  Derive your class from an interface, for example, IMyInterface.
2.  Include [**DECLARE\_IUNKNOWN**](declare-iunknown.md) in your class definition to declare implementations of **QueryInterface**, **AddRef**, and **Release** that call the outer unknown.
3.  Override **NonDelegatingQueryInterface** to expose IMyInterface with code such as the following:
    ```C++
         if (riid == IID_IMyInterface) {
             return GetInterface((IMyInterface *) this, ppv);
         } else {
             return CUnknown::NonDelegatingQueryInterface(riid, ppv);
         }
    ```

    

4.  Declare and implement the member functions of IMyInterface.

To use `INonDelegatingUnknown` for nested interfaces, perform the following steps:

1.  Declare a class derived from [**CUnknown**](cunknown.md).
2.  Include [**DECLARE\_IUNKNOWN**](declare-iunknown.md) in your class definition.
3.  Override **NonDelegatingQueryInterface** to expose IMyInterface with the code such as the following:
    ```C++
         if (riid == IID_IMyInterface) {
             return GetInterface((IMyInterface *) this, ppv);
         } else {
             return CUnknown::NonDelegatingQueryInterface(riid, ppv);
         }
    ```

    

4.  Implement the member functions of IMyInterface. Use [**CUnknown::GetOwner**](cunknown-getowner.md) to access the COM object class.
5.  In your COM object class, make the nested class a friend of the COM object class, and declare an instance of the nested class as a member of the COM object class.

Because you must always pass the outer unknown and an **HRESULT** to the [**CUnknown**](cunknown.md) constructor, you can't use a default constructor. You have to make the member variable a pointer to the class and make a new call in your constructor to actually create it.

Override the **NonDelegatingQueryInterface** with code such as the following:


```C++
     if (riid == IID_IMyInterface) {
         return m_pImplFilter->
            NonDelegatingQueryInterface(IID_IMyInterface, ppv);
     } else {
         return CUnknown::NonDelegatingQueryInterface(riid, ppv);
     }
```



You can have mixed classes that support some interfaces through multiple inheritance and some interfaces through nested classes.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COM Helper Functions**](com-helper-functions.md)
</dt> </dl>

 

 




