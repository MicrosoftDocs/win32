---
title: Creating a Service
description: Creating a Web service is greatly simplified in WWSAPI by the Service Model API and the WsUtil.exe tool.
ms.assetid: 3536d1c6-6179-4f69-9cc8-27fe6ae30826
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Service

Creating a Web service is greatly simplified in WWSAPI by the [Service Model](service-model-layer-overview.md) API and the [WsUtil.exe](wsutil-compiler-tool.md) tool. The Service Model provides an API that enables the service and client to send and receive [messages](message.md) over a [channel](channel.md) as C method calls. The WsUtil tool generates stubs and headers for implementing the service.

## Implementing a Calculator Service using WWSAPI

Using the generated sources from the [Wsutil.exe](wsutil-compiler-tool.md) tool, implement the service by the following steps.

Include the headers in your application source.

``` syntax
#include "CalculatorProxyStub.h"
```

Implement the service operations. In this example, the service operations are the Add and Subtract functions of the calculator service.

``` syntax
HRESULT CALLBACK Add (const WS_OPERATION_CONTEXT* context, 
                  int a, int b, int* result, 
                  const WS_ASYNC_CONTEXT* asyncContext, 
                  WS_ERROR* error)
{
    *result = a + b;
    printf ("%d + %d = %d\n", a, b, *result);
    return NOERROR;
}

HRESULT CALLBACK Subtract (const WS_OPERATION_CONTEXT* context, 
                  int a, int b, int* result, 
                  const WS_ASYNC_CONTEXT* asyncContext, 
                  WS_ERROR* error)
{
    *result = a - b;
    printf ("%d - %d = %d\n", a, b, *result);
    return NOERROR;
}
```

Define the service contract by setting the fields of a [**WS\_SERVICE\_CONTRACT**](/windows/desktop/api/WebServices/ns-webservices-ws_service_contract) structure.

``` syntax
static const DefaultBinding_ICalculatorFunctionTable calculatorFunctions = {Add, Subtract};
static const WS_SERVICE_CONTRACT calculatorContract = 
{
    &DefaultBinding_ICalculatorContractDesc, // comes from the generated header.
    NULL, // for not specifying the default contract
    &calculatorFunctions // specified by the user
};
```

Now, create a service host and open it for communication.

``` syntax
WS_SERVICE_ENDPOINT serviceEndpoint = {0};
serviceEndpoint.uri.chars = L"https://+:80/example"; // address given as uri
serviceEndpoint.binding.channelBinding =  WS_HTTP_CHANNEL_BINDING; // channel binding for the endpoint
serviceEndpoint.channelType = WS_CHANNEL_TYPE_REPLY; // the channel type
serviceEndpoint.uri.length = (ULONG)wcslen(serviceEndpoint.uri.chars);
serviceEndpoint.contract = (WS_SERVICE_CONTRACT*)&calculatorContract;  // the contract
serviceEndpoint.properties = serviceProperties;
serviceEndpoint.propertyCount = WsCountOf(serviceProperties);

if (FAILED (hr = WsCreateServiceHost (&serviceEndpoint, 1, NULL, 0, &host, error)))
    goto Error;

// WsOpenServiceHost  to start the listeners in the service host 
if (FAILED (hr = WsOpenServiceHost (host, NULL, error)))
    goto Error;
```

Please refer to the code example at [HttpCalculatorServiceExample](httpcalculatorserviceexample.md) for a full implementation of the calculator service.

 

 




