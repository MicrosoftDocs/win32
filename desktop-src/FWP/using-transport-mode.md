---
title: Using Transport Mode
description: Following sample code demonstrates how to configure IPsec transport mode using AuthIP with user authentication and negotiation discovery.
ms.assetid: 996d2fc9-ed88-4c96-93f0-a4e5daf7dc45
ms.topic: article
ms.date: 05/31/2018
---

# Using Transport Mode

The following sample code demonstrates how to configure IPsec transport mode using AuthIP with user authentication and negotiation discovery.


```C++
#include <winsock2.h>
#include <fwpmu.h>
#include <mstcpip.h>
#include <stdio.h>

#pragma comment(lib, "fwpuclnt.lib")
#pragma comment(lib, "crypt32.lib")
#pragma comment(lib, "rpcrt4.lib")

#define EXIT_ON_ERROR(fnName) \
   if (result != ERROR_SUCCESS) \
   { \
      printf(#fnName " = 0x%08X\n", result); \
      goto CLEANUP; \
   }
   
DWORD ConfigureIPsecTransportMode(
         __in HANDLE engine,
         __in PCWSTR policyName,
         __in_opt const GUID* providerKey,
         __in PCWSTR rootCertSubject
         )
{
   DWORD result = ERROR_SUCCESS;
   HCERTSTORE certStore = NULL;
   PCCERT_CONTEXT rootCert = NULL;
   IKEEXT_CERT_ROOT_CONFIG0 certRootConfig;
   BOOL txnInProgress = FALSE;
   IKEEXT_AUTHENTICATION_METHOD0 mmAuthMethods[2];
   IKEEXT_PROPOSAL0 mmProposals[2];
   IKEEXT_POLICY0 mmPolicy;
   FWPM_PROVIDER_CONTEXT0 provCtxt;
   FWPM_FILTER0 filter;
   IKEEXT_AUTHENTICATION_METHOD0 emAuthMethods[2];
   IKEEXT_EM_POLICY0 emPolicy;
   const IPSEC_SA_LIFETIME0 qmLifetime =
   {
      3600,       // lifetimeSeconds
      100000,     // lifetimeKilobytes
      0x7FFFFFFF  // lifetimePackets
   };
   IPSEC_AUTH_TRANSFORM0 qmTransform00;
   IPSEC_SA_TRANSFORM0 qmTransforms0[1];
   IPSEC_AUTH_TRANSFORM0 qmTransform10;
   IPSEC_SA_TRANSFORM0 qmTransforms1[1];
   IPSEC_AUTH_AND_CIPHER_TRANSFORM0 qmTransform20;
   IPSEC_SA_TRANSFORM0 qmTransforms2[1];
   IPSEC_AUTH_AND_CIPHER_TRANSFORM0 qmTransform30;
   IPSEC_SA_TRANSFORM0 qmTransforms3[1];
   IPSEC_PROPOSAL0 qmProposals[4];
   IPSEC_TRANSPORT_POLICY0 qmPolicy;
   FWPM_FILTER_CONDITION0 filterConditions[2];

   // Open the local machine's CA certificate store.
   certStore = CertOpenStore(
                  CERT_STORE_PROV_SYSTEM,
                  0,
                  0,
                  ( CERT_STORE_OPEN_EXISTING_FLAG |
                    CERT_STORE_READONLY_FLAG |
                    CERT_SYSTEM_STORE_LOCAL_MACHINE),
                  L"Root"
                  );
   result = (certStore != NULL) ? ERROR_SUCCESS : GetLastError();
   EXIT_ON_ERROR(CertOpenStore);

   // Find the specified root certificate.
   rootCert = CertFindCertificateInStore(
                 certStore,
                 (X509_ASN_ENCODING | PKCS_7_ASN_ENCODING),
                 0,
                 CERT_FIND_SUBJECT_STR,
                 rootCertSubject,
                 NULL
                 );
   result = (rootCert != NULL) ? ERROR_SUCCESS : GetLastError();
   EXIT_ON_ERROR(CertFindCertificateInStore);

   // The CERT_INFO.Subject name blob is already in the format expected by
   // AuthIP.
   memset(&certRootConfig, 0, sizeof(certRootConfig));
   certRootConfig.certData.size = rootCert->pCertInfo->Subject.cbData;
   certRootConfig.certData.data = rootCert->pCertInfo->Subject.pbData;

   // We add all the objects from within a single transaction to make it easy
   // to clean up partial results in error paths.
   result = FwpmTransactionBegin0(engine, 0);
   EXIT_ON_ERROR(FwpmTransactionBegin0);
   txnInProgress = TRUE;

   memset(mmAuthMethods, 0, sizeof(mmAuthMethods));

   // Primary main mode auth method is Kerberos. This is the most efficient for
   // domain-joined machines.
   mmAuthMethods[0].authenticationMethodType = IKEEXT_KERBEROS;

   // Secondary main mode auth method is SSL. This allows non-joined machines
   // to authenticate as well provided they have been provisioned with an
   // appropriate certificate.
   mmAuthMethods[1].authenticationMethodType = IKEEXT_SSL;
   mmAuthMethods[1].sslAuthentication.inboundConfigType =
      IKEEXT_CERT_CONFIG_EXPLICIT_TRUST_LIST;
   mmAuthMethods[1].sslAuthentication.inboundRootArraySize = 1;
   mmAuthMethods[1].sslAuthentication.inboundRootArray = &certRootConfig;
   mmAuthMethods[1].sslAuthentication.outboundConfigType =
      IKEEXT_CERT_CONFIG_EXPLICIT_TRUST_LIST;
   mmAuthMethods[1].sslAuthentication.outboundRootArraySize = 1;
   mmAuthMethods[1].sslAuthentication.outboundRootArray = &certRootConfig;
   // Disable CRL checks for test purposes. Consider enabling them in real use.
   mmAuthMethods[1].sslAuthentication.flags =
      IKEEXT_CERT_AUTH_FLAG_DISABLE_CRL_CHECK;

   // Configure two main mode proposals: AES-128/SHA-1 & 3DES/SHA-1 each with a
   // lifetime of 8 hours. Fallback to 3DES might be desirable to allow some
   // servers to use 3DES for performance reasons.
   memset(mmProposals, 0, sizeof(mmProposals));
   mmProposals[0].cipherAlgorithm.algoIdentifier = IKEEXT_CIPHER_AES_128;
   mmProposals[0].integrityAlgorithm.algoIdentifier = IKEEXT_INTEGRITY_SHA1;
   mmProposals[0].maxLifetimeSeconds = 8 * 60 * 60;
   mmProposals[1].cipherAlgorithm.algoIdentifier = IKEEXT_CIPHER_3DES;
   mmProposals[1].integrityAlgorithm.algoIdentifier = IKEEXT_INTEGRITY_SHA1;
   mmProposals[1].maxLifetimeSeconds = 8 * 60 * 60;

   memset(&mmPolicy, 0, sizeof(mmPolicy));
   mmPolicy.numAuthenticationMethods = ARRAYSIZE(mmAuthMethods);
   mmPolicy.authenticationMethods = mmAuthMethods;
   mmPolicy.numIkeProposals = ARRAYSIZE(mmProposals);
   mmPolicy.ikeProposals = mmProposals;

   memset(&provCtxt, 0, sizeof(provCtxt));
   // We have to assign the key ourselves since we will need it when adding the
   // filters that reference this provider context.
   result = UuidCreate(&(provCtxt.providerContextKey));
   EXIT_ON_ERROR(UuidCreate);
   // For MUI compatibility, object names should be indirect strings. See
   // SHLoadIndirectString for details.
   provCtxt.displayData.name = (PWSTR)policyName;
   // Link all our objects to our provider. When multiple providers are
   // installed on a computer, this makes it easy to determine who added what.
   provCtxt.providerKey = (GUID*)providerKey;
   provCtxt.type = FWPM_IPSEC_AUTHIP_MM_CONTEXT;
   provCtxt.authIpMmPolicy = &mmPolicy;

   // Add the main mode policy.
   result = FwpmProviderContextAdd0(engine, &provCtxt, NULL, NULL);
   EXIT_ON_ERROR(FwpmProviderContextAdd0);

   // Add filters referencing the policy to the IKEEXT policy layers. 
   // We could also add remote address conditions to the filters to 
   // limit which machines or subnets are protected. Note that we use the same 
   // main mode policy for both IPv4 and IPv6.
   memset(&filter, 0, sizeof(filter));
   filter.displayData.name = (PWSTR)policyName;
   filter.flags = FWPM_FILTER_FLAG_HAS_PROVIDER_CONTEXT;
   filter.providerKey = (GUID*)providerKey;
   // Policy filters should always have an action type of PERMIT.
   filter.action.type = FWP_ACTION_PERMIT;
   filter.providerContextKey = provCtxt.providerContextKey;

   filter.layerKey = FWPM_LAYER_IKEEXT_V4;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   filter.layerKey = FWPM_LAYER_IKEEXT_V6;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   // Allow two extended mode authentication methods: Kerberos for
   // domain-joined machines and NTLMv2 for non-joined machines.
   memset(&emAuthMethods, 0, sizeof(emAuthMethods));
   emAuthMethods[0].authenticationMethodType = IKEEXT_KERBEROS;
   emAuthMethods[1].authenticationMethodType = IKEEXT_NTLM_V2;

   memset(&emPolicy, 0, sizeof(emPolicy));
   emPolicy.numAuthenticationMethods = ARRAYSIZE(emAuthMethods);
   emPolicy.authenticationMethods = emAuthMethods;
   emPolicy.initiatorImpersonationType = IKEEXT_IMPERSONATION_SOCKET_PRINCIPAL;

   memset(qmProposals, 0, sizeof(qmProposals));

   // First QM proposal is AH. This is preferable to ESP auth since 
   // more routers are capable of parsing AH.
   memset(&qmTransform00, 0, sizeof(qmTransform00));
   qmTransform00.authTransformId = IPSEC_AUTH_TRANSFORM_ID_HMAC_SHA_1_96;
   memset(qmTransforms0, 0, sizeof(qmTransforms0));
   qmTransforms0[0].ipsecTransformType = IPSEC_TRANSFORM_AH;
   qmTransforms0[0].ahTransform = &qmTransform00;
   qmProposals[0].lifetime = qmLifetime;
   qmProposals[0].numSaTransforms = ARRAYSIZE(qmTransforms0);
   qmProposals[0].saTransforms = qmTransforms0;

   // Second QM proposal is ESP auth. This might be necessary for NAT
   // traversal.
   memset(&qmTransform10, 0, sizeof(qmTransform10));
   qmTransform10.authTransformId = IPSEC_AUTH_TRANSFORM_ID_HMAC_SHA_1_96;
   memset(&qmTransforms1, 0, sizeof(qmTransforms1));
   qmTransforms1[0].ipsecTransformType = IPSEC_TRANSFORM_ESP_AUTH;
   qmTransforms1[0].espAuthTranform = &qmTransform10;
   qmProposals[1].lifetime = qmLifetime;
   qmProposals[1].numSaTransforms = ARRAYSIZE(qmTransforms1);
   qmProposals[1].saTransforms = qmTransforms1;

   // Third QM proposal is ESP auth and cipher using AES-128. This will
   // allow remote peers to require encryption if necessary.
   memset(&qmTransform20, 0, sizeof(qmTransform20));
   qmTransform20.authTransform.authTransformId =
      IPSEC_AUTH_TRANSFORM_ID_HMAC_SHA_1_96;
   qmTransform20.cipherTransform.cipherTransformId =
      IPSEC_CIPHER_TRANSFORM_ID_AES_128;
   memset(&qmTransforms2, 0, sizeof(qmTransforms2));
   qmTransforms2[0].ipsecTransformType = IPSEC_TRANSFORM_ESP_AUTH_AND_CIPHER;
   qmTransforms2[0].espAuthAndCipherTransform = &qmTransform20;
   qmProposals[2].lifetime = qmLifetime;
   qmProposals[2].numSaTransforms = ARRAYSIZE(qmTransforms2);
   qmProposals[2].saTransforms = qmTransforms2;

   // Fourth QM proposal allows fallback to 3DES for perf reasons.
   memset(&qmTransform30, 0, sizeof(qmTransform30));
   qmTransform30.authTransform.authTransformId =
      IPSEC_AUTH_TRANSFORM_ID_HMAC_SHA_1_96;
   qmTransform30.cipherTransform.cipherTransformId =
      IPSEC_CIPHER_TRANSFORM_ID_CBC_3DES;
   memset(&qmTransforms3, 0, sizeof(qmTransforms3));
   qmTransforms3[0].ipsecTransformType = IPSEC_TRANSFORM_ESP_AUTH_AND_CIPHER;
   qmTransforms3[0].espAuthAndCipherTransform = &qmTransform30;
   qmProposals[3].lifetime = qmLifetime;
   qmProposals[3].numSaTransforms = ARRAYSIZE(qmTransforms3);
   qmProposals[3].saTransforms = qmTransforms3;

   memset(&qmPolicy, 0, sizeof(qmPolicy));
   qmPolicy.numIpsecProposals = ARRAYSIZE(qmProposals);
   qmPolicy.ipsecProposals = qmProposals;
   // Set ND_SECURE since we require IPsec for all inbound connections.
   // This flag alone doesn't guarantee enforcement and is only used to
   // ensure connectivity in IPsec+NAT scenarios.
   qmPolicy.flags = IPSEC_POLICY_FLAG_ND_SECURE;
   qmPolicy.ndAllowClearTimeoutSeconds = 10;
   qmPolicy.saIdleTimeout.idleTimeoutSeconds = 300;
   qmPolicy.saIdleTimeout.idleTimeoutSecondsFailOver = 60;
   qmPolicy.emPolicy = &emPolicy;

   memset(&provCtxt, 0, sizeof(provCtxt));
   result = UuidCreate(&(provCtxt.providerContextKey));
   EXIT_ON_ERROR(UuidCreate);
   provCtxt.displayData.name = (PWSTR)policyName;
   provCtxt.providerKey = (GUID*)providerKey;
   provCtxt.type = FWPM_IPSEC_AUTHIP_QM_TRANSPORT_CONTEXT;
   provCtxt.authipQmTransportPolicy = &qmPolicy;

   // Add the main mode policy.
   result = FwpmProviderContextAdd0(engine, &provCtxt, NULL, NULL);
   EXIT_ON_ERROR(FwpmProviderContextAdd0);

   // Add filters referencing the policy to the IPsec policy layers.
   // As above, we could also add remote address conditions to the 
   // filters to limit which machines or subnets are protected. 
   // Note that we use the same quick mode policy for both IPv4 and IPv6.
   memset(&filter, 0, sizeof(filter));
   filter.displayData.name = (PWSTR)policyName;
   filter.flags = FWPM_FILTER_FLAG_HAS_PROVIDER_CONTEXT;
   filter.providerKey = (GUID*)providerKey;
   filter.action.type = FWP_ACTION_PERMIT;
   filter.providerContextKey = provCtxt.providerContextKey;

   filter.layerKey = FWPM_LAYER_IPSEC_V4;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   filter.layerKey = FWPM_LAYER_IPSEC_V6;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   // We only protect unicast traffic.
   memset(filterConditions, 0, sizeof(filterConditions));
   filterConditions[0].fieldKey = FWPM_CONDITION_IP_LOCAL_ADDRESS_TYPE;
   filterConditions[0].matchType = FWP_MATCH_EQUAL;
   filterConditions[0].conditionValue.type = FWP_UINT8;
   filterConditions[0].conditionValue.uint8 = NlatUnicast;

   // Fields common to all transport and ALE IPsec callout filters.
   memset(&filter, 0, sizeof(filter));
   filter.displayData.name = (PWSTR)policyName;
   filter.providerKey = (GUID*)providerKey;
   filter.action.type = FWP_ACTION_CALLOUT_TERMINATING;
   filter.numFilterConditions = 1;
   filter.filterCondition = filterConditions;
   filter.providerContextKey = provCtxt.providerContextKey;

   filter.layerKey = FWPM_LAYER_OUTBOUND_TRANSPORT_V4;
   filter.action.calloutKey = FWPM_CALLOUT_IPSEC_OUTBOUND_TRANSPORT_V4;
   filter.rawContext = FWPM_CONTEXT_IPSEC_OUTBOUND_NEGOTIATE_DISCOVER;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   filter.layerKey = FWPM_LAYER_OUTBOUND_TRANSPORT_V6;
   filter.action.calloutKey = FWPM_CALLOUT_IPSEC_OUTBOUND_TRANSPORT_V6;
   filter.rawContext = FWPM_CONTEXT_IPSEC_OUTBOUND_NEGOTIATE_DISCOVER;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   filter.layerKey = FWPM_LAYER_INBOUND_TRANSPORT_V4;
   filter.action.calloutKey = FWPM_CALLOUT_IPSEC_INBOUND_TRANSPORT_V4;
   filter.rawContext = FWPM_CONTEXT_IPSEC_INBOUND_PERSIST_CONNECTION_SECURITY;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   filter.layerKey = FWPM_LAYER_INBOUND_TRANSPORT_V6;
   filter.action.calloutKey = FWPM_CALLOUT_IPSEC_INBOUND_TRANSPORT_V6;
   filter.rawContext = FWPM_CONTEXT_IPSEC_INBOUND_PERSIST_CONNECTION_SECURITY;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   filter.layerKey = FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4;
   filter.action.calloutKey = FWPM_CALLOUT_IPSEC_INBOUND_INITIATE_SECURE_V4;
   filter.rawContext = FWPM_CONTEXT_IPSEC_INBOUND_PERSIST_CONNECTION_SECURITY;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   filter.layerKey = FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6;
   filter.action.calloutKey = FWPM_CALLOUT_IPSEC_INBOUND_INITIATE_SECURE_V6;
   filter.rawContext = FWPM_CONTEXT_IPSEC_INBOUND_PERSIST_CONNECTION_SECURITY;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   // Next we'll add filters to exempt ICMP traffic.
   filterConditions[1].fieldKey = FWPM_CONDITION_IP_PROTOCOL;
   filterConditions[1].matchType = FWP_MATCH_EQUAL;
   filterConditions[1].conditionValue.type = FWP_UINT8;
   filterConditions[1].conditionValue.uint8 = IPPROTO_ICMP;

   memset(&filter, 0, sizeof(filter));
   filter.displayData.name = (PWSTR)policyName;
   filter.providerKey = (GUID*)providerKey;
   filter.weight.type = FWP_UINT8;
   // The exemptions must be added at a higher weight range to ensure 
   // that they will match before the IPsec callout filters added above.
   filter.weight.uint8 = FWPM_WEIGHT_RANGE_IKE_EXEMPTIONS;
   filter.action.type = FWP_ACTION_CALLOUT_TERMINATING;
   filter.numFilterConditions = 2;
   filter.filterCondition = filterConditions;
   filter.action.type = FWP_ACTION_PERMIT;

   filter.layerKey = FWPM_LAYER_OUTBOUND_TRANSPORT_V4;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   filter.layerKey = FWPM_LAYER_INBOUND_TRANSPORT_V4;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   filter.layerKey = FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V4;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   filterConditions[1].conditionValue.uint8 = IPPROTO_ICMPV6;

   filter.layerKey = FWPM_LAYER_OUTBOUND_TRANSPORT_V6;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   filter.layerKey = FWPM_LAYER_INBOUND_TRANSPORT_V6;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   filter.layerKey = FWPM_LAYER_ALE_AUTH_RECV_ACCEPT_V6;
   result = FwpmFilterAdd0(engine, &filter, NULL, NULL);
   EXIT_ON_ERROR(FwpmFilterAdd0);

   // Once all the adds have succeeded, we commit the transaction to 
   // add all the new objects atomically.
   result = FwpmTransactionCommit0(engine);
   EXIT_ON_ERROR(FwpmTransactionCommit0);
   txnInProgress = FALSE;

CLEANUP:
   if (txnInProgress)
   {
      // Abort any transaction still in progress to clean up 
      // partial results.
      FwpmTransactionAbort0(engine);
   }
   if (rootCert != NULL)
   {
      CertFreeCertificateContext(rootCert);
   }
   if (certStore != NULL)
   {
      CertCloseStore(certStore, CERT_CLOSE_STORE_CHECK_FLAG);
   }
   return result;
}
```



 

 




