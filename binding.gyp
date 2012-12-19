{
	'variables': {
		# Default for this variable, to get the right behavior for
		# Node versions <= 0.6.*.
		'node_shared_openssl%': 'true'
	},
	'targets': [
		{
			'target_name': 'ursaNative',
			'sources': [ 'src/ursaNative.cc' ],
			'conditions': [
			
			
				[ 'OS=="win"', {
				  'conditions': [
					# "openssl_root" is the directory on Windows of the OpenSSL files
					['target_arch=="x64"', {
					  'variables': {
						'openssl_root%': 'C:/OpenSSL-Win64'
					  },
					}, {
					  'variables': {
						'openssl_root%': 'C:/OpenSSL-Win32'
					  },
					}],
				  ],
				  'defines': [
					'uint=unsigned int',
				  ],
				  'libraries': [ 
					'-l<(openssl_root)/lib/libeay32.lib',
				  ],
				  'include_dirs': [
					'<(openssl_root)/include',
				  ],
				}, { # OS!="win"
				  'include_dirs': [
					# use node's bundled openssl headers on Unix platforms
					'<(node_root_dir)/deps/openssl/openssl/include'
				  ],
				  'conditions': [
					[ 'node_shared_openssl=="false"', {
						'include_dirs': [
							'<(node_root_dir)/deps/openssl/openssl/include'
						]
					}]
					]
				}],
			
			]
		}
	]
}
