package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	var files []string = make([]string, 0)
	filepath.Walk(".", func(path string, info os.FileInfo, err error) error {
		if !info.IsDir() {
			var path, err = filepath.Abs(path)
			if err == nil {
				files = append(files, path)
			}
		}
		return nil
	})
	fmt.Println(files)
}
