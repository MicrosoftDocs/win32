---
title: SSO Password Change Behavior
description: Provides a step-by-step approach for resolving SSO password change behavior.
ms.assetid: 'c52ffeb8-ecee-4398-a7df-388b523c737c'
---

# SSO Password Change Behavior

This topic provides a step-by-step approach for resolving SSO password change behavior.

## Step-By-Step Approach

The following list represents a step-by-step approach for resolving SSO password change behavior.

-   Once the EAP method is notified about a password change, the method notifies EAPHost; EAPHost in turn notifies the supplicant by returning the action code, [EapHostPeerResponseInvokeUI](eaphostpeerresponseaction.md).
-   After receiving the [EapHostPeerResponseInvokeUI](eaphostpeerresponseaction.md) action code from EAPHost, the supplicant obtains the UI context from the EAP method by calling the [**EapHostPeerGetUIContext**](eaphostpeergetuicontext.md) function; EAPHost then obtains the UI context from the EAP method by calling the corresponding method function
-   The supplicant passes the UI context to the UI process (using some form of inter-process communication).
-   The UI process calls [**EapHostPeerQueryInteractiveUIInputFields**](eaphostpeerqueryinteractiveuiinputfields.md) on EAPHost.
-   EAPHost collects the UI context by calling [**EapPeerQueryInteractiveUIInputFields**](eappeerqueryinteractiveuiinputfields.md) on the EAP method.
-   The EAP method provides any necessary UI context information in the [**EAP\_INTERACTIVE\_UI\_DATA**](eap-interactive-ui-data.md) structure, where *dwDataType* is set to *EapCredExpiryReq* and *pbUiData* points to a structure of type [**EAP\_CRED\_REQ**](eap-cred-req.md).
-   While populating the [**EAP\_INTERACTIVE\_UI\_DATA**](eap-interactive-ui-data.md) structure, this EAP method will only fill in the *curCreds* parameter, and not set the [**EAP\_UI\_INPUT\_FIELD\_PROPS\_READ\_ONLY**](eap-config-input-field-data.md) flag in the **EAP\_CONFIG\_INPUT\_FIELD\_DATA** structure.
    > [!Note]  
    > The [**EAP\_UI\_INPUT\_FIELD\_PROPS\_READ\_ONLY**](eap-config-input-field-data.md) flag is for member field(s) which need to be changed.

     

-   Having collected the UI context informtion, the UI process renders a UI to collect change password information from the user. This information is populated in the *NewCreds* parameter of the [**EAP\_CRED\_EXPIRY\_REQ**](eap-cred-expiry-req.md) structure.
-   The UI process passes the [**EAP\_CRED\_RESP**](eap-cred-resp.md) structure back to EAPHost via [**EapHostPeerQueryUIBlobFromInteractiveUIInputFields**](eaphostpeerqueryuiblobfrominteractiveuiinputfields.md).
-   The UI process passes this user BLOB to the supplicant, and the supplicant continues with EAPHost run-time functions as usual.

## Related topics

<dl> <dt>

[SSO EAPHost Scenarios](why-eaphost-sso.md)
</dt> <dt>

[SSO and PLAP](understanding-sso-and-plap.md)
</dt> </dl>

 

 




