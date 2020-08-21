---
title: ' in, out, string Prototype'
description: The following function prototype uses a single \ in, out, string\ parameter for both the input and output strings.
ms.assetid: 5a652b79-11ca-4780-aac1-60a22f96b4af
ms.topic: article
ms.date: 05/31/2018
---

# \[in, out, string\] Prototype

The following function prototype uses a single \[[**in**](/windows/desktop/Midl/in), [**out**](/windows/desktop/Midl/out-idl), [**string**](/windows/desktop/Midl/string)\] parameter for both the input and output strings. The string first contains patient input and is then overwritten with the doctor response as shown:

``` syntax
void Analyze([in, out, string, size_is(STRSIZE)] char  achInOut[]);
```

This example is similar to the one that employed a single-counted string for both input and output. As with that example, the \[[**size\_is**](/windows/desktop/Midl/size-is)\] attribute determines the number of elements allocated on the server. The \[[**string**](/windows/desktop/Midl/string)\] attribute directs the stub to call **strlen** to determine the number of transmitted elements.

The client allocates all memory before the call as:

``` syntax
/* client */
char achInOut[STRSIZE];
...
gets_s(achInOut, STRSIZE);            // get patient input
Analyze(achInOut);
printf("%s\n", achInOut);  // display doctor response
```

Note that the Analyze function no longer must calculate the length of the return string as it did in the counted-string example where the **\[string\]** attribute was not used. Now the stubs calculate the length as shown:

``` syntax
/* server */
void Analyze(char *pchInOut)
{
   ...
   Respond(response, pchInOut); // don't need to call strlen
   return;                      // stubs handle size
}
```

 

 