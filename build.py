import base64
B64_TARGETS = ["TARGET_VUE_JS"]

TARGETS = {"TARGET_RNODE_JS":          "./js/rnode.js",
           "TARGET_DFU_FLASHER_JS":    "./js/nrf52_dfu_flasher.js",
           "TARGET_ZIP_JS":            "./js/zip.min.js",
           "TARGET_TAILWIND_JS":       "./js/tailwindcss/tailwind-v3.4.3-forms-v0.5.7.js",
           "TARGET_VUE_JS":            "./js/vue@3.4.26/dist/vue.global.js",
           "TARGET_CRYPTO_CORE_JS":    "./js/crypto-js@3.9.1-1/core.js",
           "TARGET_CRYPTO_MD5_JS":     "./js/crypto-js@3.9.1-1/md5.js",
           "TARGET_ESPTOOL_BUNDLE_JS": "./js/esptool-js@0.4.5/bundle.js",
           "TARGET_SERIAL_JS":         "./js/web-serial-polyfill@1.0.15/dist/serial.js",
           }

def compile_html():
	for b64_target in B64_TARGETS:
		if b64_target in TARGETS:
			src_path = TARGETS[b64_target]
			with open(src_path, "rb") as src_file:
				b64 = base64.b64encode(src_file.read())
				TARGETS[b64_target] = b64

	with open("template.html", "rb") as template_file:
		template = template_file.read().decode("utf-8")
		for target in TARGETS:
			target_str = "{"+target+"}"
			src_path   = TARGETS[target]

			if target in B64_TARGETS:
				print(f"Inserting base64 for {target}...")
				template = template.replace(target_str, TARGETS[target].decode("utf-8"))

			else:
				print(f"Inserting {target} from {src_path}...")
				with open(src_path, "rb") as source_file:
					src = source_file.read().decode("utf-8")
					template = template.replace(target_str, src)

		with open("RNode_Flasher.html", "wb") as compiled_file:
			compiled_file.write(template.encode("utf-8"))

	print("Done!")

if __name__ == "__main__":
	print("Compiling HTML file...")
	compile_html()
