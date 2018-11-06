---
title: Server Annotation Sample
description: Server Annotation Sample
ms.assetid: 8e87a2ca-236c-4082-acf5-dc3807dde6bc
ms.topic: article
ms.date: 05/31/2018
---

# Server Annotation Sample

The following is an example of server annotation. Follow instructions in comments marked with /\* TODO \*/.


```C++
// 
//  Skeleton code for class which implements IAccPropServer 
// 

class CMyAccPropServer: public IAccPropServer
{
    ULONG               m_Ref;
    IAccPropServices *  m_pAccPropSvc;

public:

    AccServerBase( IAccPropServices * pAccPropSvc )
        : m_Ref( 1 ),
          m_pAccPropSvc( pAccPropSvc )
    {
        m_pAccPropSvc->AddRef();
    }

    ~AccServerBase()
    {
        m_pAccPropSvc->Release();
    }

    
    /* TODO: Addref/Release/QI go here...
     */

    HRESULT STDMETHODCALLTYPE GetPropValue (const BYTE * pIDString,
        DWORD dwIDStringLen, MSAAPROPID idProp, VARIANT * pvarValue,
        BOOL * pfGotProp )
    {
        // Clear out parameters, in case we return early... 
        pvarValue->vt = VT_EMPTY;
        *pfGotProp = FALSE;
        
        /*  TODO: if you need to access internal data structures, you should
         *  verify that they still exist here. If they no longer exist,
         *  return CO_E_OBJNOTCONNECTED.
         */

        // Figure out which child this request is for... 
        HWND  hwnd;
        DWORD idObject;
        DWORD idChild;

        if( S_OK != m_pAccPropSvc->DecomposeHwndIdentityString( pIDString, 
                  dwIDStringLen, & hwnd, & idObject, & idChild ) )
        {
            // problem decomposing identity string - return early... 
            return S_OK;
        }

        
        /*  TODO: You need to determine which child ids you 
         *  want to handle properties for. Change this 
         *  if or extend it into an if/else/if
         *  to handle each id you need.
         *
         *  To handle all the children of an object, but not 
         *  the parent object itself, 
         *  use "if (idChild != CHILDID_SELF )" as the 
         *  condition.
         */

        if( idChild == CHILDID_SELF )
        {
            
            /*  TODO: change or extend this if(...) for each 
             *  property you are overriding.
             *
             *  The constants for the properties are (from 
             *  oleacc.h):
             *    
             *    PROPID_ACC_NAME
             *    PROPID_ACC_VALUE
             *    PROPID_ACC_DESCRIPTION
             *    PROPID_ACC_ROLE
             *    PROPID_ACC_STATE
             *    PROPID_ACC_HELP
             *    PROPID_ACC_KEYBOARDSHORTCUT
             *    PROPID_ACC_DEFAULTACTION
             *
             *    PROPID_ACC_FOCUS
             *    PROPID_ACC_SELECTION
             *    PROPID_ACC_PARENT
             *
             *    PROPID_ACC_NAV_UP
             *    PROPID_ACC_NAV_DOWN
             *    PROPID_ACC_NAV_LEFT
             *    PROPID_ACC_NAV_RIGHT
             *    PROPID_ACC_NAV_PREV
             *    PROPID_ACC_NAV_NEXT
             *    PROPID_ACC_NAV_FIRSTCHILD
             *    PROPID_ACC_NAV_LASTCHILD
             *
             */
            if( idProp == PROPID_ACC_ROLE )
            {
                
                /*  TODO: lookup or otherwise determine the 
                 *  value you want to return for this 
                 *  property of this child.
                 *
                 *  Note that idChild is a 1-based index of 
                 *  a child element, so you'll need to 
                 *  subtract 1 if you use 0-based indices.
                 *
                 *  If you have a value to return, set 
                 *  pvarValue to that value,
                 *  and set *pfGotProp to TRUE.
                 *
                 *  If you have no value to return, do 
                 *  nothing. (*pfGotProp
                 *  will be FALSE from above.)
                 */

                // For example, pretend that everything is a menu item:
                pvarValue.vt = VT_I4;
                pvarValue.lVal = ROLE_SYSTEM_MENUITEM;

                *pfGotProp = TRUE;
            }
        }

        return S_OK;
    }
};


[ ... ]

// 
//  Skeleton code to register class which implements IAccPropServer
// 
//  Do this after the corresponding HWND is created. 
// 
//  Perf tip: instead of doing this immediately after the HWND is created, 
//  you can delay it until that HWND receives its first WM_GETOBJECT message. 
//  This delays the CoCreate until necessary. You will need to subclass the 
//  HWND to catch the WM_GETOBJECT. After registering, pass the WM_GETOBJECT 
//  on to the original window proc for the HWND. 
// 


    IAccPropServices * pAccPropSvc = NULL;
    HRESULT hr;
    hr = CoCreateInstance( CLSID_AccPropServices, NULL,
            CLSCTX_SERVER, IID_IAccPropServices, (void **) & pAccPropSvc ));
    if( hr == S_OK && pAccPropSvc )
    {
        CMyAccPropServer* pMyPropSrv = new CMyAccPropServer( pAccPropSvc );
        if( pMyPropSrv )
        {
            
            /*  TODO: extend this array if you are 
             *  overriding multiple properties.
             *  Make sure to update the length parameter 
             *  passed to SetHwndPropServer
             *  so that it matches the number of elements in 
             *  this array.
             */
            MSAAPROPID propids[ 1 ];
            propids[ 0 ] = PROPID_ACC_ROLE;

            
            /*  TODO: Specify the appropriate objid and 
             *  childid here. The idObject will
             *  nearly always be OBJID_CLIENT. Use a childid 
             *  of CHILD_CLIENT to refer to
             *  a container or an overall object, or use a 
             *  1-based index to refer to a
             *  specific child item in that container.
             * 
             *  To override properties of all elements in a 
             *  container, use CHILDID_SELF,
             *  and specify the ANNO_CONTAINER in the last 
             *  parameter.
             */
            pAccPropSvc->SetHwndPropServer( hwnd, OBJID_CLIENT,
                    CHILDID_SELF, & propid, 1, pMyPropSrv, 0 );
            pMyPropSrv->Release();
            pAccPropSvc->Release();
        }
    }
```



 

 




