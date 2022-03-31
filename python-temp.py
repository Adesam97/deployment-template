  resources = [{
      'name': '<name>',
      'type': 'compute.v1.instance',
      'properties': {
          'zone': '<zone>',
          'machineType': ''.join([COMPUTE_URL_BASE, 'projects/MY_PROJECT',
                                  '/zones/<zone>/',
                                  'machineTypes/f1-micro']),
          'disks': [{
              'deviceName': 'boot',
              'type': 'PERSISTENT',
              'boot': True,
              'autoDelete': True,
              'initializeParams': {
                  'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/',
                                          'debian-cloud/global/',
                                          'images/family/debian-9'])
              }
          }],
          'networkInterfaces': [{
              'network': '$(ref.a-new-network.selfLink)',
              'accessConfigs': [{
                  'name': 'External NAT',
                  'type': 'ONE_TO_ONE_NAT'
              }]
          }]
      }
  }]
  return {'resources': resources}

  # for importing when vm template are more than one

imports:
- path: vm-template.py
- path: vm-template-2.py

# In the resources section, the properties of the resources are replaced
# with the names of the templates.
resources:
- name: vm-1
  type: vm-template.py
- name: vm-2
  type: vm-template-2.py
- name: a-new-network
  type: compute.v1.network
  properties:
    routingConfig:
      routingMode: REGIONAL
    autoCreateSubnetworks: true


