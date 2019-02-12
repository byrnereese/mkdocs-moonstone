# Syntax Highlighting

## Inline

Morbi eget `dapibus felis`. Vivamus *`venenatis porttitor`* tortor sit amet
rutrum. Class aptent taciti sociosqu ad litora torquent per conubia nostra,
per inceptos himenaeos. [`Pellentesque aliquet quam enim`](#), eu volutpat urna
rutrum a.

Nam vehicula nunc `:::js return target` mauris, a ultricies libero efficitur
sed. Sed molestie imperdiet consectetur. Vivamus a pharetra leo. Pellentesque
eget ornare tellus, ut gravida mi. Fusce vel lacinia lacus.

### Highlight Line Numbers

    #!js hl_lines="8"
    var _extends = function(target) {
      for (var i = 1; i < arguments.length; i++) {
        var source = arguments[i];
        for (var key in source) {
          target[key] = source[key];
        }
      }
      return target;
    };

## Tabbed Code Blocks

Multiple code blocks in a row will automatically be grouped into a set of tabs. This utilizes the [superfences](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/) markdown extension.

```c tab=
printf("HELLO WORLD!");
```

```java tab=
System.out.println("HELLO WORLD!");
```

```python tab=
print("HELLO WORLD!")
```
