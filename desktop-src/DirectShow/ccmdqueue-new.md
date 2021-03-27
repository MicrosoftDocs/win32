---
description: The New method initializes a command to be run and returns a new CDeferredCommand object.
ms.assetid: bdd80747-a15b-422a-b742-ebfa4076bdf7
title: CCmdQueue.New method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCmdQueue.New
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CCmdQueue.New method

The `New` method initializes a command to be run and returns a new [**CDeferredCommand**](cdeferredcommand.md) object.

## Syntax


```C++
virtual HRESULT New(
   CDeferredCommand **ppCmd,
   LPUNKNOWN        pUnk,
   REFTIME          time,
   GUID             *iid,
   long             dispidMethod,
   short            wFlags,
   long             cArgs,
   VARIANT          *pDispParams,
   VARIANT          *pvarResult,
   short            *puArgErr,
   BOOL             bStream
);
```



## Parameters

<dl> <dt>

*ppCmd* 
</dt> <dd>

Address of a pointer to a [**CDeferredCommand**](cdeferredcommand.md) object by which an application can cancel the command, set a new presentation time for it, or retrieve estimate information.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the object that will run the command.

</dd> <dt>

*time* 
</dt> <dd>

Time at which to run the queued command or commands.

</dd> <dt>

*iid* 
</dt> <dd>

Pointer to the globally unique identifier (**GUID**) of the interface to call.

</dd> <dt>

*dispidMethod* 
</dt> <dd>

Method on the interface to be called.

</dd> <dt>

*wFlags* 
</dt> <dd>

Flags describing the context of the call. This parameter supports the same flags as the **IDispatch::Invoke** method.

</dd> <dt>

*cArgs* 
</dt> <dd>

Number of arguments passed.

</dd> <dt>

*pDispParams* 
</dt> <dd>

Pointer to the list of variant types associated with the dispatch parameters.

</dd> <dt>

*pvarResult* 
</dt> <dd>

Pointer to the list where results, if any, are to be returned.

</dd> <dt>

*puArgErr* 
</dt> <dd>

Pointer to the index within the *pDispParams* parameter list where the last error occurred.

</dd> <dt>

*bStream* 
</dt> <dd>

Value indicating whether the *time* parameter is a stream-time value (**TRUE**) or a presentation-time value (**FALSE**).

</dd> </dl>

## Return value

Returns S\_OK if successful. Returns E\_OUTOFMEMORY if *ppCmd* returns from creating the new [**CDeferredCommand**](cdeferredcommand.md) object with a value of **NULL**. Otherwise, returns an **HRESULT** that indicates an error from attempting to create a new **CDeferredCommand** object. If there is an error, no object has been queued.

## Remarks

The new [**CDeferredCommand**](cdeferredcommand.md) object will be initialized with the parameters and will be added to the queue during construction. This method is similar to the **IDispatch::Invoke** method.

Values for the *wFlags* parameter include the following:



| Value                    | Description                                                                                                                                                          |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DISPATCH\_METHOD         | The member is being run as a method. If a property has the same name, both this and the DISPATCH\_PROPERTYGET flag can be set.                                       |
| DISPATCH\_PROPERTYGET    | The member is being retrieved as a property or data member.                                                                                                          |
| DISPATCH\_PROPERTYPUT    | The member is being changed as a property or data member.                                                                                                            |
| DISPATCH\_PROPERTYPUTREF | The member is being changed via a reference assignment, rather than a value assignment. This value is valid only when the property accepts a reference to an object. |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCmdQueue Class**](ccmdqueue.md)
</dt> </dl>

 

 




