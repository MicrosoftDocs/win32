---
title: SSO EAP-TLS PIN Caching Behavior
description: Provides a step-by-step approach for resolving matters of session resumption and re-authentication of a roaming user in an SSO EAP-TLS environment.
ms.assetid: aeded6c9-315d-4115-9750-485f017dd8dd
ms.topic: article
ms.date: 05/31/2018
---

# SSO EAP-TLS PIN Caching Behavior

This topic provides a step-by-step approach for resolving matters of session resumption and re-authentication of a roaming user in an SSO EAP-TLS environment.

## Step-By-Step Approach

The following list represents a step-by-step approach for resolving matters of session resumption and re-authentication of a roaming user in an SSO EAP-TLS environment.

-   After the first successful authentication in an SSO environment with EAP-TLS, the supplicant retains all user credential related information by default.
    > [!Note]  
    > Although subject to the particular supplicant implementation, it's advisable for the supplicant to retain the entire [**EAP\_CONFIG\_INPUT\_FIELD ARRAY**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_config_input_field_array) structure that the supplicant last used in the [**EapHostPeerQueryUserBlobFromCredentialInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerqueryuserblobfromcredentialinputfields) call to EAPHost.

     

-   As the user first roams and the re-authentication begins, the supplicant calls [**EapHostPeerQueryUserBlobFromCredentialInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerqueryuserblobfromcredentialinputfields) again with the same [**EAP\_CONFIG\_INPUT\_FIELD ARRAY**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_config_input_field_array) structure; the supplicant must also pass in the same user BLOB retained after the first successful authentication.
-   EAPHost then passes the information in the user BLOB to the EAP method.
-   The EAP method in turn updates the user BLOB with credential fields - the PIN for example - provided in *pEapConfigInputFieldArray*, and keeps the remaining values - the server certificate for example - as it was in the original user BLOB.
-   After completing these steps, the supplicant can resume authentication in a normal way by calling the [**EapHostPeerBeginSession**](/previous-versions/windows/desktop/api/eappapis/nf-eappapis-eaphostpeerbeginsession) run-time function with this user BLOB.

## Related topics

<dl> <dt>

[SSO EAPHost Scenarios](why-eaphost-sso.md)
</dt> <dt>

[SSO and PLAP](understanding-sso-and-plap.md)
</dt> </dl>

 

 




