import json
import logging

import requests


class RocketChatHandler(logging.Handler):
   def __init__(self, webhook_url):
       logging.Handler.__init__(self)
       self.webhook_url = webhook_url
   def emit(self, record):
      log_entry = self.format(record)
      payload = {
            "text": log_entry
        }
      headers = {'Content-Type': 'application/json'}
      if record.levelno == logging.CRITICAL:
      requests.post(self.webhook_url, data=f"```\n {json.dumps(payload)} \n ```", headers=headers)


# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set this to your needed level

# Set up Rocket.Chat handler
webhook_url = "https://rc.atro.xyz/hooks/64c2d9c1b57f1ebcf31d70a7/nKFcoBJQuYoiNAZ9rhMYJxE4rG5WGiRcspSNkX2vZDTQaDhg"
rocketchat_handler = RocketChatHandler(webhook_url)
rocketchat_handler.setLevel(logging.FATAL)

# Set up a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rocketchat_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(rocketchat_handler)

# Test the logger
logger.debug("This is a debug log.")
logger.info("This is an info log.")
logger.warning("This is a warning log.")
logger.error("This is an error log.")
logger.critical("This is a critical log.")
logger.fatal("This is a fatal log.")

logger.fatal('''
             JavaScriptError:

  Error: There is already a Construct with name 'HajimariApplication' in Chart [chart]
      at Node.addChild (/tmp/jsii-kernel-XJE7sN/node_modules/constructs/lib/construct.js:352:19)
      at new Node (/tmp/jsii-kernel-XJE7sN/node_modules/constructs/lib/construct.js:38:21)
      at new Construct (/tmp/jsii-kernel-XJE7sN/node_modules/constructs/lib/construct.js:409:21)
      at new ApiObject (/tmp/jsii-kernel-XJE7sN/node_modules/cdk8s/lib/api-object.js:59:9)
      at new Application (/tmp/jsii-kernel-XJE7sN/node_modules/iohajimari/io.hajimari.js:21:9)
      at Kernel._create (/tmp/tmpnxkhwkkm/lib/program.js:9964:29)
      at Kernel.create (/tmp/tmpnxkhwkkm/lib/program.js:9693:29)
      at KernelHost.processRequest (/tmp/tmpnxkhwkkm/lib/program.js:11544:36)
      at KernelHost.run (/tmp/tmpnxkhwkkm/lib/program.js:11504:22)
      at Immediate._onImmediate (/tmp/tmpnxkhwkkm/lib/program.js:11505:46)
The above exception was the direct cause of the following exception:
File "/app/bootstrap/bootstrap.py", line 65, in <module>
    61       ensure_cache_paths(inputs.app_name, inputs.app_namespace)
    62
    63   from entry import run
    64
--> 65   run(inputs)
    ..................................................
     inputs.app_name = 'args'
     inputs.app_namespace = 'docs'
     inputs = AtroCdk8sInputs(app_name='args', app_namespace='docs', versi
               on='0.1.*', imports_path=PosixPath('/app/generated/imports')
               , defaults_path=PosixPath('/app/defaults.yaml'), app_path=Po
               sixPath('/tmpcmpserver/197ebac2-a85c-43a3-878f-48a217a98c
               f4/apps/docs/args'), keep_app_template_cache=False, one_file
               =True, yaml_depth=3, values_file=None, dev_use_master=False)
    ..................................................
File "/home/atropos/.cache/atrocdk8s/apps/args.docs/core/entry.py", line 105, in run
    96   def run(inputs: AtroCdk8sInputs):
 (...)
   101          modules=[sys.modules[__name__]],
   102          packages=["functions", "functions.network", "functions.volumes"],
   103      )
   104
-> 105      execute()
   ..................................................
    inputs = AtroCdk8sInputs(app_name='args', app_namespace='docs', versi
              on='0.1.*', imports_path=PosixPath('/app/generated/imports')
              , defaults_path=PosixPath('/app/defaults.yaml'), app_path=Po
              sixPath('/tmpcmpserver/197ebac2-a85c-43a3-878f-48a217a98c
              f4/apps/docs/args'), keep_app_template_cache=False, one_file
              =True, yaml_depth=3, values_file=None, dev_use_master=False)
    sys.modules = {'sys': <module 'sys' (built-in)>,
                   'builtins': <module 'builtins' (built-in)>,
                   frozenimportlib': <module frozenimportlib' (frozen)>,
                   imp': <module 'imp' (built-in)>,
                   thread': <module 'thread' (built-in)>,
                   warnings': <module 'warnings' (built-in)>,
                   weakref': <module 'weakref' (built-in)>,
                   io': <module 'io' (built-in)>,
                   'marshal': <module 'marshal' (built-in)>,
                   'posix': <module 'posix' (built-in)>,
                   frozenimportlib_external': <module frozenimportlib_ex
                   ternal' (f...
    __name__ = 'entry'
   ..................................................
ile "src/dependency_injectorcwiring.pyx", line 28, in dependencyinjectorcwiring.get_sync_patched._patched
ile "/home/atropos/.cache/atrocdk8s/apps/args.docs/core/entry.py", line 25, in execute
   23   @inject
   24   def execute(app: cdk8s.App = Provide[AtroContainer.app]):
-> 25       execute_hajimaris()
   26       execute_ingress_route()
   ..................................................
    app = <cdk8s.App object at 0x7f3f2afa90>
   ..................................................
ile "src/dependency_injectorcwiring.pyx", line 28, in dependencyinjectorcwiring.get_sync_patched._patched
ile "/home/atropos/.cache/atrocdk8s/apps/args.docs/core/functions/hajimari.py", line 23, in execute_hajimaris
   15   def execute_hajimaris(
   16       chart=Provide[AtroContainer.chart],
   17       metadata: ApiObjectMetadata = Provide[AtroContainer.cdk8s_metadata],
   18       id: AtroId = Provide[AtroContainer.id],
   19       routes: AtroRoutes = Provide[AtroContainer.routes],
   20   ):
   21       for route in routes:
   22           if route.hajimari_enabled and route.domains:
-> 23               application = Application(
   24                   chart,
   ..................................................
    chart = <cdk8s.Chart object at 0x7f3e8b4f10>
    metadata = ApiObjectMetadata(labels={'app.kubernetes.io/name': 'args',
                'app.kubernetes.io/instance': 'args', 'app.kubernetes.io/man
                aged-by': 'atrocdk8s'}, name='args', namespace='docs')
    id = AtroId(name='args', namespace='docs')
    routes = AtroRoutes(routes=[AtroRoute(name='web', protocol='TCP', por
              t=8000, target_port=8000, domains=['args-docs.atro.xyz'], in
              fo='', icon='bar-chart', auth=False, hajimari_enabled=True,
              ingress_route_enabled=True), AtroRoute(name='webhook', proto
              col='TCP', port=8080, target_port=8080, domains=['args-docs-
              webhook.atro.xyz'], info='', icon='bar-chart', auth=False, h
              ajimari_enabled=True, ingress_route_enabled=True)])
    route = AtroRoute(name='webhook', protocol='TCP', port=8080, target_
             port=8080, domains=['args-docs-webhook.atro.xyz'], info='',
             icon='bar-chart', auth=False, hajimari_enabled=True, ingress
             routeenabled=True)
    route.hajimari_enabled = True
    route.domains = ['args-docs-webhook.atro.xyz', ]
    application = <imports.io.hajimari.Application object at 0x7f3e856390>
   ..................................................
ile "/usr/local/lib/python3.11/site-packages/jsii/_runtime.py", line 112, in __call__
   111  def __call__(cls: Type[Any], args: Any, *kwargs) -> Any:
-> 112      inst = super().__call__(args, *kwargs)
   113
   ..................................................
    args = (<cdk8s.Chart object at 0x7f3e8b4f10>, 'HajimariApplication'
            , )
    kwargs = {'metadata': ApiObjectMetadata(labels={'app.kubernetes.io/na
              me': 'args', 'app.kubernetes.io/instance': 'args', 'app.kube
              rnetes.io/managed-by': 'atrocdk8s'}, name='args', namespace=
              'docs'),
              'spec': ApplicationSpec(group='docs', name='args', url='htt
              ps://args-docs-webhook.atro.xyz', icon='bar-chart', info='')
              }
   ..................................................
ile "/app/generated/imports/io/hajimari/__init__.py", line 47, in __init__
   26   def __init__(
   27       self,
   28       scope: constructs77d1e7e8.Construct,
   29       id: builtins.str,
   30       *,
   31       metadata: typing.Optional[typing.Unioncdk8sd3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
   32       spec: typing.Optional[typing.Union["ApplicationSpec", typing.Dict[builtins.str, typing.Any]]] = None,
   33   ) -> None:
(...)
   43           check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
   44           check_type(argname="argument id", value=id, expected_type=type_hints["id"])
   45       props = ApplicationProps(metadata=metadata, spec=spec)
   46
-> 47       jsii.create(self.__class__, self, [scope, id, props])
   ..................................................
    self = <imports.io.hajimari.Application object at 0x7f3e83f8d0>
    scope = <cdk8s.Chart object at 0x7f3e8b4f10>
    id = 'HajimariApplication'
    metadata = ApiObjectMetadata(labels={'app.kubernetes.io/name': 'args',
                'app.kubernetes.io/instance': 'args', 'app.kubernetes.io/man
                aged-by': 'atrocdk8s'}, name='args', namespace='docs')
    spec = ApplicationSpec(group='docs', name='args', url='https://args
            -docs-webhook.atro.xyz', icon='bar-chart', info='')
    type_hints = {'scope': <class 'constructs.Construct'>,
                  'id': <class 'str'>,
                  'metadata': typing.Union[cdk8s.ApiObjectMetadata, typing.Di
                  ct[str, typing.Any], NoneType],
                  'spec': typing.Union[imports.io.hajimari.ApplicationSpec, t
                  yping.Dict[str, typing.Any], NoneType],
                  'return': <class 'NoneType'>}
    props = ApplicationProps(metadata=ApiObjectMetadata(labels={'app.kub
             ernetes.io/name': 'args', 'app.kubernetes.io/instance': 'arg
             s', 'app.kubernetes.io/managed-by': 'atrocdk8s'}, name='args
             ', namespace='docs'), spec=ApplicationSpec(group='docs', nam
             e='args', url='https://args-docs-webhook.atro.xyz', icon='ba
             r-chart', info=''))
    jsii.create = <method 'Kernel.create' of <jsii._kernel.Kernel object at 0x
                   7f8459e710> __init__.py:330>
   ..................................................
ile "/usr/local/lib/python3.11/site-packages/jsiikernel/_init__.py", line 334, in create
   330  def create(self, klass: Type, obj: Any, args: Optional[List[Any]] = None) -> ObjRef:
   331      if args is None:
   332          args = []
   333
-> 334      response = self.provider.create(
   335          CreateRequest(
   ..................................................
    self = <jsii._kernel.Kernel object at 0x7f8459e710>
    obj = <imports.io.hajimari.Application object at 0x7f3e83f8d0>
    args = [<cdk8s.Chart object at 0x7f3e8b4f10>, 'HajimariApplication'
            , ApplicationProps(metadata=ApiObjectMetadata(labels={'app.k
            ubernetes.io/name': 'args', 'app.kubernetes.io/instance': 'a
            rgs', 'app.kubernetes.io/managed-by': 'atrocdk8s'}, name='ar
            gs', namespace='docs'), spec=ApplicationSpec(group='docs', n
            ame='args', url='https://args-docs-webhook.atro.xyz', icon='
            bar-chart', info='')), ]
    self.provider.create = <method 'ProcessProvider.create' of <jsii._kernel.providers.
                            process.ProcessProvider object at 0x7f84311d10> process.py:3
                            62>
   ..................................................
ile "/usr/local/lib/python3.11/site-packages/jsii/_kernel/providers/process.py", line 363, in create
   362  def create(self, request: CreateRequest) -> CreateResponse:
-> 363      return self._process.send(request, CreateResponse)
   ..................................................
    self = <jsii._kernel.providers.process.ProcessProvider object at 0x
            7f84311d10>
    request = CreateRequest(fqn='iohajimari.Application', args=[<cdk8s.Cha
               rt object at 0x7f3e8b4f10>, 'HajimariApplication', {'$jsii.s
               truct': {'fqn': 'iohajimari.ApplicationProps', 'data': {'met
               adata': {'$jsii.struct': {'fqn': 'cdk8s.ApiObjectMetadata',
               'data': {'annotations': None, 'finalizers': None, 'labels':
               {'$jsii.map': {'app.kubernetes.io/name': 'args', 'app.kubern
               etes.io/instance': 'args', 'app.kubernetes.io/managed-by': '
               atrocdk8s'}}, 'name': 'args', 'namespace': 'docs', 'ownerRef
               erences': None}}}, '...
    selfprocess.send = <method 'NodeProcess.send' of <jsii._kernel.providers.proce
                          ss._NodeProcess object at 0x7f84190c10> process.py:318>
   ..................................................
ile "/usr/local/lib/python3.11/site-packages/jsii/_kernel/providers/process.py", line 340, in send
   318  def send(
   319      self, request: KernelRequest, response_type: Type[KernelResponse]
   320  ) -> KernelResponse:
(...)
   336          return resp.callback
   337      else:
   338          if resp.name == ErrorType.JSII_FAULT.value:
   339              raise JSIIError(resp.error) from JavaScriptError(resp.stack)
-> 340          raise RuntimeError(resp.error) from JavaScriptError(resp.stack)
   ..................................................
    self = <jsiikernel.providers.process.NodeProcess object at 0x7f8
            4190c10>
    request = CreateRequest(fqn='iohajimari.Application', args=[<cdk8s.Cha
               rt object at 0x7f3e8b4f10>, 'HajimariApplication', {'$jsii.s
               truct': {'fqn': 'iohajimari.ApplicationProps', 'data': {'met
               adata': {'$jsii.struct': {'fqn': 'cdk8s.ApiObjectMetadata',
               'data': {'annotations': None, 'finalizers': None, 'labels':
               {'$jsii.map': {'app.kubernetes.io/name': 'args', 'app.kubern
               etes.io/instance': 'args', 'app.kubernetes.io/managed-by': '
               atrocdk8s'}}, 'name': 'args', 'namespace': 'docs', 'ownerRef
               erences': None}}}, '...
    resp.callback = # AttributeError
         resp = _ErrorResponse(error="There is already a Construct wi
          th name 'HajimariApplication' in Chart [chart]", stack="Erro
          r: There is already a Construct with name 'HajimariApplicati
          on' in Chart [chart]\n    at Node.addChild (/tmp/jsii-kernel
          -XJE7sN/node_modules/constructs/lib/construct.js:352:19)\n
            at new Node (/tmp/jsii-kernel-XJE7sN/node_modules/construc
          ts/lib/construct.js:38:21)\n    at new Construct (/tmp/jsii-
          kernel-XJE7sN/node_modules/constructs/lib/construct.js:409:2
          1)\\...
    resp.name = 'Error'
    ErrorType.JSII_FAULT.value = '@jsii/kernel.Fault'
    resp.error = "There is already a Construct with name 'HajimariApplication
                  ' in Chart [chart]"
    resp.stack = "Error: There is already a Construct with name 'HajimariAppl
                  ication' in Chart [chart]\n    at Node.addChild (/tmp/jsii-k
                  ernel-XJE7sN/node_modules/constructs/lib/construct.js:352:19
                  )\n    at new Node (/tmp/jsii-kernel-XJE7sN/node_modules/con
                  structs/lib/construct.js:38:21)\n    at new Construct (/tmp/
                  jsii-kernel-XJE7sN/node_modules/constructs/lib/construct.js:
                  409:21)\n    at new ApiObject (/tmp/jsii-kernel-XJE7sN/node_
                  modules/cdk8s/lib/api-object.js:59:9)\n    at new Applicatio
                  n (/tmp/jsii-kernel-...
   ..................................................
--- (full traceback above) ----
ile "/app/bootstrap/bootstrap.py", line 65, in <module>
   run(inputs)
ile "/home/atropos/.cache/atrocdk8s/apps/args.docs/core/entry.py", line 105, in run
   execute()
ile "src/dependency_injectorcwiring.pyx", line 28, in dependencyinjectorcwiring.get_sync_patched._patched
ile "/home/atropos/.cache/atrocdk8s/apps/args.docs/core/entry.py", line 25, in execute
   execute_hajimaris()
ile "src/dependency_injectorcwiring.pyx", line 28, in dependencyinjectorcwiring.get_sync_patched._patched
ile "/home/atropos/.cache/atrocdk8s/apps/args.docs/core/functions/hajimari.py", line 23, in execute_hajimaris
   application = Application(
ile "/usr/local/lib/python3.11/site-packages/jsii/_runtime.py", line 112, in __call__
   inst = super().__call__(args, *kwargs)
ile "/app/generated/imports/io/hajimari/__init__.py", line 47, in __init__
   jsii.create(self.__class__, self, [scope, id, props])
ile "/usr/local/lib/python3.11/site-packages/jsiikernel/_init__.py", line 334, in create
   response = self.provider.create(
ile "/usr/local/lib/python3.11/site-packages/jsii/_kernel/providers/process.py", line 363, in create
   return self._process.send(request, CreateResponse)
ile "/usr/local/lib/python3.11/site-packages/jsii/_kernel/providers/process.py", line 340, in send
   raise RuntimeError(resp.error) from JavaScriptError(resp.stack)
untimeError: There is already a Construct with name 'HajimariApplication' in Chart [chart]
''')
