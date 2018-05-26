---
title: Invoking a Service-Defined Method
description: Services are represented by Service objects, which are a specialized type of WPDObject that supports methods.
ms.assetid: 9c9eeaa2-4407-43ee-8222-d795821315f9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Invoking a Service-Defined Method

Services are represented by [**Service**](service-object.md) objects, which are a specialized type of [**WPDObject**](wpdobject.md) that supports methods.

A **Service** object makes available all of the methods that have been defined for the service that it represents. (See the [**Service.Method**](service-method.md) reference page for more information on this.) It also provides an [**on*Method*Complete event**](service-onmethodcomplete.md) so that event handlers can be written based on the completion of these service-defined methods.

> [!Note]  
> For service-defined methods, the actual method name should be used in place of Method. For example, if a service supports the *DoSomething* method, the completion event will be on*DoSomething*Complete.

 

The parameters of service methods are defined by the service. The results of service methods can be returned as named parameters. The parameter names are specified by the service implementation of the target device.

WPD Automation infers the method signature depending on the parameter type specified in the method definition.

-   Input parameters are passed into the method function.
-   Output parameters should be returned as properties of the method Result.
-   Input/output parameters are both passed into the method function and returned as a property of the method Result.

For example, a service method is defined as follows:

Sample Method Definition:

Name = "MyMethod"

Parameters, Count = 3

1.  "StringParam1", in, string.
2.  "IntegerParam2", out, integer.
3.  "StringParam3", in/out, string.

In WPD Automation, the following function is provided:

`var Results = ServiceObject.MyMethod(StringParam1, StringParam3);`

Where:

Value of IntegerParam2 = Results.IntegerParam2

Value of StringParam3 = Results.StringParam3

Note that since "StringParam1" is an input parameter, it is not available as a property of the Results object.

The following example is a JScript function that demonstrates how to retrieve a service by Persistent Unique ID (PUID) and invoke a service-defined method, returning one of its results.


```JScript
function CallServiceMethod()
{
   // Retrieve a service from the device by using its PUID.
   var aService = deviceObject.Services[aServicePUID];

   // Invoke the method.
   var results = aService.MyMethod("Test Input String", "Test In/Output String");

   // Store the results returned by the service method.
   var intParam2 = results.Param2;
   var stringParam3 = results.Param3; 

   // Return the output integer result.
   return intParam2;    
}
```



## Related topics

<dl> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> <dt>

[WPD Automation Programming Guide](wpd-automation-programming-guide.md)
</dt> </dl>

 

 




