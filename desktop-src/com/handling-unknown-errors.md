---
title: Handling Unknown Errors
description: Handling Unknown Errors
ms.assetid: d6a4cc60-8320-4b67-9f2e-7c4bea6c37fb
ms.topic: article
ms.date: 05/31/2018
---

# Handling Unknown Errors

It is legal to return a status code only from the implementation of an interface method sanctioned as legally returnable. Failure to observe this rule invites the possibility of conflict between returned error-code values and those sanctioned by the application. Pay particular attention to this potential problem when propagating error codes from functions that are called internally.

Applications that call interfaces should treat any unknown returned error code (as opposed to a success code) as synonymous with E\_UNEXPECTED. This practice of handling unknown error codes is required by clients of the COM-defined interfaces and functions. Because typical programming practice is to handle a few specific error codes in detail and treat the rest generically, this requirement of handling unexpected or unknown error codes is easily met.

It is important to handle all possible errors when calling an interface method. Failure to do so could cause your application to crash, to corrupt data, or to become vulnerable to security exploits. The following code sample shows the recommended way of handling unknown errors:


```C++
HRESULT hr; 
hr = xxMethod(); 
 
switch (GetScode(hr))  
{ 
    case NOERROR: 
      // Method returned success. 
      break; 
 
    case x1: 
      // Handle error x1 here.
      break; 
 
    case x2: 
      // Handle error x2 here.
      break; 
 
    case E_UNEXPECTED: 
    default: 
      // Handle unexpected errors here. 
      break; 
} 
 
```



The following error check is often used with those routines that do not return anything special (other than S\_OK or some unexpected error):


```C++
if (xxMethod() == NOERROR) 
{
    // Handle success here.
} 
else 
{
    // Handle failure here.
} 
```



## Related topics

<dl> <dt>

[Error Handling in COM](error-handling-in-com.md)
</dt> </dl>

 

 




