name = "bob"
greeting = f"Hello, {name}"

print(greeting)

#Template

aname = "var"
agreeting = "hello, {}"
with_aname = agreeting.format(aname)


print(with_aname)

longer_phrase = "Hello, {}, Today is {}."
formatted = longer_phrase.format("pra", "mon")

print(formatted)
