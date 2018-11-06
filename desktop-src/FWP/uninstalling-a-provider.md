---
title: Uninstalling a Provider
description: Following sample code demonstrates the process required to remove a provider installation.
ms.assetid: fe86972f-f1fb-41b8-989e-f146dba0bd06
ms.topic: article
ms.date: 05/31/2018
---

# Uninstalling a Provider

The following sample code demonstrates the process required to remove a provider installation.


```C++
// Illustrates common tasks a provider might perform during uninstall: deleting
// a persistent provider and sublayer.

#include <windows.h>
#include <fwpmu.h>
#include <stdio.h>

#pragma comment(lib, "fwpuclnt.lib")

#define EXIT_ON_ERROR(fnName) \
   if (result != ERROR_SUCCESS) \
   { \
      printf(#fnName " = 0x%08X\n", result); \
      goto CLEANUP; \
   }

#define SESSION_NAME L"SDK Examples"

// 5fb216a8-e2e8-4024-b853-391a4168641e
const GUID PROVIDER_KEY =
{
   0x5fb216a8,
   0xe2e8,
   0x4024,
   { 0xb8, 0x53, 0x39, 0x1a, 0x41, 0x68, 0x64, 0x1e }
};

DWORD Uninstall(
         __in const GUID* providerKey,
         __in const GUID* subLayerKey
         )
{
   DWORD result = ERROR_SUCCESS;
   HANDLE engine = NULL;
   FWPM_SESSION0 session;

   memset(&session, 0, sizeof(session));
   // The session name isn't required but may be useful for diagnostics.
   session.displayData.name = SESSION_NAME;
   // Set an infinite wait timeout, so we don't have to handle FWP_E_TIMEOUT
   // errors while waiting to acquire the transaction lock.
   session.txnWaitTimeoutInMSec = INFINITE;

   // The authentication service should always be RPC_C_AUTHN_DEFAULT.
   result = FwpmEngineOpen0(
               NULL,
               RPC_C_AUTHN_DEFAULT,
               NULL,
               &session,
               &engine
               );
   EXIT_ON_ERROR(FwpmEngineOpen0);

   // We delete the provider and sublayer from within a single transaction, so
   // that we always leave the system in a consistent state even in error
   // paths.
   result = FwpmTransactionBegin0(engine, 0);
   EXIT_ON_ERROR(FwpmTransactionBegin0);

   // We have to delete the sublayer first since it references the provider. If
   // we tried to delete the provider first, it would fail with FWP_E_IN_USE.
   result = FwpmSubLayerDeleteByKey0(engine, subLayerKey);
   if (result != FWP_E_SUBLAYER_NOT_FOUND)
   {
      // Ignore FWP_E_SUBLAYER_NOT_FOUND. This allows uninstall to succeed even
      // if the current configuration is broken.
      EXIT_ON_ERROR(FwpmSubLayerDeleteByKey0);
   }

   result = FwpmProviderDeleteByKey0(engine, providerKey);
   if (result != FWP_E_PROVIDER_NOT_FOUND)
   {
      EXIT_ON_ERROR(FwpmProviderDeleteByKey0);
   }

   // Once all the deletes have succeeded, we commit the transaction to
   // atomically delete all the objects.
   result = FwpmTransactionCommit0(engine);
   EXIT_ON_ERROR(FwpmTransactionCommit0);

CLEANUP:
   // FwpmEngineClose0 accepts null engine handles, so we needn't precheck for
   // null. Also, when closing an engine handle, any transactions still in
   // progress are automatically aborted, so we needn't explicitly abort the
   // transaction in error paths.
   FwpmEngineClose0(engine);
   return result;
}
```



 

 




